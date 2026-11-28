# guaidao2/Trail

⭐ 3 · Go · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/guaidao2/Trail) · 个人维护 · 中文 README

**蓝队与运维人员的 AI 服务器运维与安全研判中枢**

以 Go 编写的单二进制 Web 平台：通过 SSH/Telnet 纳管主机（无需在目标机装 agent），提供定期巡检、日志攻击检测、基线审计（GB/T 22239-2019 / CIS）、IOC 库、威胁情报订阅与可审计取证报告。核心机制为 Eino 编排的 agent（单 agent 及 Plan-Execute、Supervisor 多 agent 模式）、MCP 工具、56 条 YAML 工具配方、RAG 知识库与人审批准环节；高危命令受 RBAC 与审批门控并全部写入审计日志。从 CyberStrikeAI fork 而来，移除了红队功能。需 Go 1.25+ 与 Python 3.10+ 环境，git clone 后经 run.sh 一键构建部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 个子 agent、12 个角色提示词、56 条运维与蓝队工具配方
- 10 套日志攻击规则集（SQLi/XSS/WebShell 等）与跨行关联
- 7 组基线审计对照 GB/T 22239-2019 三级与 CIS
- 威胁情报接入 Shodan InternetDB/GreyNoise/OTX 等免 key 源

## 适用场景

- 对自有服务器定期巡检并留存可审计报告
- 安全事件发生时用 agent 做日志取证与 IOC 关联研判
- 按等保三级/CIS 做基线合规检查
- 统一管理主机凭据与远程命令执行

## 场景标签

`网络安全` `多智能体` `RAG` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L9: **Trail is the AI execution hub for server operations and blue-team security—where routine ops intent becomes govern
> L11: Trail puts planning, execution, human oversight, evidence, and replay in one auditable workspace: onboard a host an
> L46: - 🤖 **Agentic execution** translates natural-language intent into governed, auditable security actions.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `e5300aa54dc3` · [字段定义](../../DATASET.md)*
