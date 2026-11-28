# zhaji2333/ck-finder

⭐ 10 · TypeScript · MIT · 推送 2026-08-18 · [GitHub](https://github.com/zhaji2333/ck-finder) · 个人维护 · 中文 README

**面向授权渗透测试与 SRC 挖洞的 LLM Agent 工具**

以确定性信息收集引擎（ck-recon）与 LLM 决策编排结合的渗透测试/SRC 漏洞挖掘 Agent，流程覆盖资产测绘、自动挖洞、确定性验证（nuclei/sqlmap）、AI 初审与人工复审、报告导出与通杀分析。内置 Scope Gate、六条安全红线与审计留痕，前端为 Vue3 Web 指挥台（7 个 Tab）。依赖 Node.js ≥22.19、PostgreSQL、Redis，未填 LLM 密钥时 LLM 环节降级为纯规则。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性信息收集引擎：子域枚举、DNS、端口扫描、指纹、FOFA、ICP 备案反查
- planner/worker Agent 编排挖洞，支持引导提示词与登录凭据注入
- 确定性验证与证据五件套（poc/raw_request/raw_response/kill_chain/self_check）
- Scope Gate + R1-R6 安全红线 + 全量审计留痕

## 适用场景

- 对已授权目标做子域枚举、端口扫描与攻击面测绘
- 批量自动化挖洞并由 AI 初审后人工裁决漏洞
- 从公司名反查 ICP 备案域名扩展 SRC 资产范围
- 导出含复现 POC 与攻击链的 Markdown 报告

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L6: 基于 pi（`@earendil-works/pi-agent-core`）的 **渗透测试 / SRC 漏洞挖掘 Agent** —— 内置确定性信息收集引擎 + LLM 决策编排 + 自动化验证 + 漏洞复审，一套闭环的混合架构
> L21: **核心理念**：**工具出数据，模型出决策** —— 收集走可靠管道（省 token），决策与验证走 LLM Agent（灵活），确定性验证与 LLM 互为兜底。
> L42: ### 自动挖洞（Agent 编排）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `085754528fd3` · [字段定义](../../DATASET.md)*
