# henry0hai/browser-n8n-local

⭐ 32 · Python · MIT · 推送 2026-09-27 · [GitHub](https://github.com/henry0hai/browser-n8n-local) · 个人维护

**让 n8n 本地对接 Browser Use 的桥接服务，替代云端 API**

本地运行的 FastAPI 桥接服务：模拟 Browser Use Cloud API 端点（含 v4 的 Run/Session/Browser 资源），使 n8n 的社区节点可直接指向本地服务器执行浏览器自动化任务，无需依赖云服务。任务运行基于 Browser Use Python 库的 agent，支持 OpenAI、Anthropic、Google、Ollama、DeepSeek、Azure OpenAI、Bedrock 等多种模型提供方，可按任务或全局配置切换。提供任务管理（运行/暂停/恢复/停止）、截图与 DOM 快照观测、每任务轨迹存储，以及自动启发式评分加人工反馈的混合奖励机制。安装方式为克隆源码并 pip 安装依赖，需 Python 3.10+ 与至少一个模型提供方的 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 实现 Browser Use Cloud v4 API 兼容端点，n8n 社区节点可指向本地服务
- 支持 OpenAI、Anthropic、Google、Ollama、DeepSeek、Azure、Bedrock 等多种模型提供方
- 截图 + DOM 快照观测与每任务轨迹存储
- 自动启发式评分与人工反馈结合的混合奖励机制

## 适用场景

- 在 n8n 工作流中执行浏览器自动化任务而不依赖 Browser Use 云服务
- 通过自然语言任务驱动浏览器操作（如打开网页并总结内容）
- 调试浏览器 agent 行为：回放轨迹、查看截图与页面状态

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: This is a local bridge service that enables n8n to communicate with the Browser Use Python library. It mimics the Br
> L8: - Supports OpenAI, Anthropic, Google, Ollama, DeepSeek, Azure OpenAI, and Bedrock providers
> L113: This bridge also implements the **Run**, **Session**, and **Browser** resources of the Browser Use Cloud v4 API, s

## 星数曲线

```mermaid
xychart-beta
    title "henry0hai/browser-n8n-local 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `15aa426f15e3` · [字段定义](../../DATASET.md)*
