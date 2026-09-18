import { pgTable, serial, varchar, integer, boolean, timestamp } from "drizzle-orm/pg-core";

export const proxies = pgTable("proxies", {
  id: serial("id").primaryKey(),
  ip: varchar("ip", { length: 255 }).notNull(),
  port: integer("port").notNull(),
  status: varchar("status", { length: 50 }).default("active").notNull(),
  failureCount: integer("failure_count").default(0).notNull(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

export const targetDomains = pgTable("target_domains", {
  id: serial("id").primaryKey(),
  domain: varchar("domain", { length: 255 }).notNull().unique(),
  strictnessLevel: varchar("strictness_level", { length: 50 }).notNull(), // low, medium, high
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

export const scrapingJobs = pgTable("scraping_jobs", {
  id: serial("id").primaryKey(),
  targetUrl: varchar("target_url", { length: 2048 }).notNull(),
  usedProxyId: integer("used_proxy_id").references(() => proxies.id),
  success: boolean("success").notNull(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});
