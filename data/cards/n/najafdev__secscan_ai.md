# najafdev/secscan_ai

⭐ 1,291 · Python · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/najafdev/secscan_ai) · [官网](https://najafdev.github.io/secscan_ai/) · 个人维护

**面向企业安全团队的 AI 驱动渗透测试平台**

云原生微服务架构的渗透测试平台，面向企业安全团队，按 6 阶段方法论（侦察、扫描、漏洞评估、利用、报告、复测）执行测试。AI 部分包括 8 家多提供商模型接入（含 OpenAI、Anthropic、DeepSeek、Ollama 等，26+ 模型、运行时切换）、CVE 威胁情报与 EPSS 评分、OWASP LLM Top 10 红队评估、SOC 日志关联与 SIEM 连接器。技术栈为 Python/Flask + PostgreSQL + Redis + Celery，支持 Docker Compose 部署 Kubernetes 编排；提供 CLI、REST API、Web 仪表盘与语音命令四种界面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 家 AI 提供商接入，26+ 模型，运行时切换与自动回退
- OWASP LLM Top 10 红队评估：25+ 对抗探针、健壮性评分
- 多云 CSPM/KSPM 审计与 CIS 基准合规检查
- Sigma 规则/Splunk SPL/Ansible Playbook 自动化修复生成

## 适用场景

- 企业安全团队对目标系统执行全流程渗透测试
- 对 LLM 应用按 OWASP Top 10 做红队评估
- 审计 AWS/Azure/GCP/Kubernetes 配置并生成修复脚本
- SOC 日志分析、IOC 提取与 SIEM 集成

## 场景标签

`网络安全` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L19: **SecScan AI Enterprise** is a production-ready, cloud-native AI-powered penetration testing platform designed for 
> L27: ### 🤖 Advanced AI Engine — Multi-Provider Support & Threat Intelligence
> L211: #### Phase 1: Intelligence Gathering & Reconnaissance


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 low · 依据 README sha `b248cafbf1e7` · [字段定义](../../DATASET.md)*
