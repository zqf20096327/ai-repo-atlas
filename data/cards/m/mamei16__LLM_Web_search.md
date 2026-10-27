# mamei16/LLM_Web_search

⭐ 284 · Python · AGPL-3.0 · 推送 2026-09-04 · [GitHub](https://github.com/mamei16/LLM_Web_search) · 个人维护

**为 text-generation-webui 本地 LLM 增加联网搜索能力的扩展**

oobabooga/text-generation-webui 的扩展：让本地 LLM 通过原生工具调用或正则匹配模型输出中的 Search_web 命令触发网页搜索，用稠密向量模型与 BM25（或 SPLADE）的集成从结果页抽取相关片段并附加到模型输出。还支持用正则触发 Download_webpage 读取网页全文（作者提示可能超出上下文长度）。通过 web UI 内的扩展安装器安装并启用，或以 python server.py --extension 方式启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 原生工具调用与自定义正则两种触发搜索的方式
- 稠密向量模型 + BM25（或 SPLADE）集成做网页片段抽取
- 正则触发网页全文读取（Download_webpage）
- 提供分块方法（语义分块与 token 分类模型分块）的说明

## 适用场景

- 本地 LLM 对话时自动检索网页补充信息
- text-generation-webui 用户为模型添加联网搜索功能
- 通过网页全文读取命令获取指定页面内容

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L1: # Give your local LLM the ability to search the web!
> L4: This project gives local LLMs the ability to search the web, either by using native tool calls or by outputting a sp

## 星数曲线

```mermaid
xychart-beta
    title "mamei16/LLM_Web_search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 283 --> 285
    line [284, 284]
```

2026-10-18 284 → 2026-10-27 284（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8aaba438d659` · [字段定义](../../DATASET.md)*
