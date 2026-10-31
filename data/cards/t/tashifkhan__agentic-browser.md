# tashifkhan/agentic-browser

⭐ 14 · Python · GPL-3.0 · 推送 2026-05-17 · [GitHub](https://github.com/tashifkhan/agentic-browser) · [官网](https://tashif.codes/u/agentic-browser) · 个人维护

**浏览器扩展形态的 AI 网页自动化 agent（MCP + Python 后端）**

WXT 浏览器扩展客户端加 Python FastAPI MCP 服务器后端的 monorepo：通过实时 DOM 检查理解网页内容，执行填表、导航、点击等 UI 自动化操作，并带语音交互、ReAct 推理、Google 搜索、Gmail 未读摘要、日历管理等斜杠命令。模型无关，可切换 OpenAI、Anthropic、Ollama、LM Studio 等后端；BYOKeys 模式，密钥与上下文本地保存。浏览器操作采用声明式动作系统，需用户逐动作批准。前端用 pnpm 构建，Python 后端由 pyproject.toml 与 uv.lock 管理，需从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时 DOM 检查理解网页并执行表单填写、导航、脚本执行等操作
- 模型无关：支持 OpenAI、Anthropic、Ollama、LM Studio 等后端切换
- MCP 协议连接浏览器与 Python FastAPI 后端
- 浏览器操作需逐动作用户批准并记录日志

## 适用场景

- 让 AI agent 代替我在网页上执行点击、填表、导航等操作
- 通过对话查询 Gmail 未读邮件、日历日程或视频内容
- 本地模型（Ollama/LLaMA）驱动的隐私优先网页自动化

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L9: **Agentic Browser** is a **next-generation browser extension** powered by a **Python MCP (Model Context Protocol) se
> L13: - **Takes actions** such as filling forms, navigating, comparing data, and executing custom scripts.

## 星数曲线

```mermaid
xychart-beta
    title "tashifkhan/agentic-browser 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `de5f459bc4ae` · [字段定义](../../DATASET.md)*
