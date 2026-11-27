# Coff0xc/catchclaw

⭐ 33 · Go · MIT · 推送 2026-11-26 · [GitHub](https://github.com/Coff0xc/catchclaw) · [官网](https://github.com/Coff0xc/catchclaw) · 个人维护

**授权式自托管 AI/LLM 平台安全评估工具箱**

单一 Go 静态二进制的安全评估工具，面向自托管 AI 基础设施（聊天 UI、agent 平台、推理服务器、向量数据库、MLOps 控制台）。在获得书面授权的目标上执行：端口扫描与 25 个平台档案的指纹识别、已知路径/默认凭据/未认证 API 探测、42 条多阶段状态传递攻击链、ATT&CK 映射的 DAG 编排（412 模块），输出 JSON/HTML/Markdown/Mermaid 报告，并可将引擎交给 Nuclei 模板、Shodan/FOFA/Hunter OSINT 或 MCP 助手。README 强调结果为未验证信号，且所有目标需事先书面授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 412 个注册模块：101 手写 exploit、269 HTTP 检查、42 条状态传递链
- 25 个平台档案覆盖 Dify、LobeChat、Open-WebUI、Ollama、vLLM、Milvus 等
- ATT&CK 阶段映射的 DAG 编排（82 条显式依赖边）
- stdio MCP 服务器，可将扫描/链/发现/OSINT 暴露给 AI 助手

## 适用场景

- 对自托管的 AI 平台做授权渗透评估
- 检测团队部署的聊天 UI/推理服务器是否存在默认凭据或未认证接口
- 将扫描能力接入 MCP 助手进行交互式安全测试

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L32: CatchClaw is a **single-binary assessment toolkit** for self-hosted AI infrastructure: chat UIs, agent platforms, i
> L36: 1. **Find** the service (port scan + keyword fingerprint across 25 profiles).
> L109: |`mcp`|Expose scan/chain/discover/nuclei/osint to an AI assistant|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `cfb4dda3e5a5` · [字段定义](../../DATASET.md)*
