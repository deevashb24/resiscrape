export interface Proxy {
  id: number;
  ip: string;
  port: number;
  status: 'active' | 'inactive' | 'banned';
  failureCount: number;
  createdAt: Date;
}

export interface TargetDomain {
  id: number;
  domain: string;
  strictnessLevel: 'low' | 'medium' | 'high';
  createdAt: Date;
}

export interface ScrapingJob {
  id: number;
  targetUrl: string;
  usedProxyId: number | null;
  success: boolean;
  createdAt: Date;
}
