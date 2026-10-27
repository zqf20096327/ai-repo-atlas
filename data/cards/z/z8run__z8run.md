# z8run/z8run

⭐ 40 · Rust · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/z8run/z8run) · [官网](https://z8run.org) · 组织维护

**Rust 编写的自托管可视化流程引擎，面向自动化与 AI 管道**

用 Rust + React 构建的开源可视化流程引擎，定位为 n8n 与 Node-RED 的自托管替代品。以 DAG 组织节点流，调度器按拓扑排序编译并行执行计划，内置 39 个节点（含 12 个 AI 节点：LLM、Embeddings、AI Agent、STT/TTS 等）与 MQTT/Twilio/CRM 集成节点。插件以 WebAssembly 沙箱运行，带资源限制。支持单二进制、源码编译与 Docker 三种部署，内嵌 SQLite 或可选 PostgreSQL，提供 AES-256-GCM 凭据库与 JWT 认证。二进制尚未代码签名。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DAG 流程引擎 + 拖拽节点编辑器，WebSocket 实时执行事件
- 39 个内置节点，含 12 个 AI 节点（LLM/Embeddings/AI Agent/STT/TTS 等）
- WebAssembly 插件沙箱（无网络/文件/时钟访问，按调用限制 CPU/时间/内存）
- 单二进制部署、内嵌 SQLite、AES-256-GCM 凭据库

## 适用场景

- 自托管搭建自动化工作流与 AI 处理管道
- 通过节点编辑器可视化编排数据流与集成（MQTT/HTTP/CRM）
- 在隔离沙箱中运行自定义插件节点

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L6:  Self-hosted alternative to n8n and Node-RED , built with Rust + React.
> L262: |**AI**|LLM, Embeddings, Classifier, Prompt Template, Text Splitter, Vector Store, Structured Output, Summarizer, 

## 星数曲线

```mermaid
xychart-beta
    title "z8run/z8run 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-27 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `63e78381f0b3` · [字段定义](../../DATASET.md)*
