# OoriData/Toolio

⭐ 139 · Python · 推送 2026-02-27 · [GitHub](https://github.com/OoriData/Toolio) · [官网](https://www.oori.dev/Toolio/) · 组织维护

**Apple Silicon 本地 LLM 服务器：JSON Schema 约束输出与工具调用**

基于 MLX 框架的 OpenAI 风格 HTTP 服务器，面向 Apple Silicon Mac（M1-M4）本地运行 MLX 格式 LLM。核心机制是把 JSON Schema 转为状态机，作为硬约束施加于输出采样器（3SO，schema 引导式结构化输出），并实现 OpenAI 规范的 tool calling，支持 pyfunc 扩展直接调用已导入的 Python 函数与内置工具库。提供 toolio_server/toolio_request 命令行与 Python API 三种使用方式；仅支持 Apple Silicon 平台，JSON Schema 支持为子集，内置工具需额外安装可选依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- JSON Schema 转状态机的硬约束结构化输出（3SO）
- OpenAI 规范 tool calling，pyfunc 扩展可调用任意可导入 Python 函数
- OpenAI 风格 HTTP 服务器 API，附命令行客户端与本地 Python API
- 附带 calculator 等内置工具（pip install toolio[tools] 安装可选依赖）

## 适用场景

- 在 Mac 上本地托管 LLM 并强制输出符合 JSON Schema 的结构化数据
- 为 agent 工作流提供带函数调用能力的本地 LLM 服务
- 从非结构化文本中按 schema 抽取实体数据

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L4: Toolio is an OpenAI-like HTTP server API implementation which supports structured LLM response generation (e.g. make
> L21: * `toolio_server` (command line)—Host MLX-format LLMs for structured output query or function calling via HTTP requ

## 星数曲线

```mermaid
xychart-beta
    title "OoriData/Toolio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 138 --> 140
    line [139, 139]
```

2026-10-18 139 → 2026-10-23 139（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2fe43dc313f4` · [字段定义](../../DATASET.md)*
