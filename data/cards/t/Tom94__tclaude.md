# Tom94/tclaude

⭐ 15 · Python · GPL-3.0 · 推送 2026-09-24 · [GitHub](https://github.com/Tom94/tclaude) · 个人维护

**面向 Anthropic Claude 的全功能终端 AI 聊天客户端**

专为 Claude 设计的终端 CLI 聊天工具：支持交互式会话（可保存/恢复/模糊查找）、扩展思考、内置联网搜索、服务端代码执行与文件上传分析、MCP 服务器（远程 OAuth2 与本地 STDIN/HTTPS 两种协议）、自动缓存与自定义 Python 工具、自定义系统提示词与任意 Anthropic 兼容端点。可通过管道集成 Unix 工作流（如 git diff 生成提交信息）。pip 安装后设置 ANTHROPIC_API_KEY 即可使用；仅支持 Claude，不支持其他 LLM。GPLv3 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持可恢复会话、扩展思考与工具调用
- 内置联网搜索、服务端代码执行与文件分析
- 支持远程与本地 MCP 服务器（OAuth2/STDIN/HTTPS）
- 可连接任意 Anthropic 兼容端点，自动缓存降低调用成本

## 适用场景

- 在终端里直接与 Claude 对话并保存恢复会话
- 通过管道把 Claude 集成进 Unix 工作流（如生成 commit message）
- 让 Claude 联网搜索、执行代码或分析上传的文件
- 通过 MCP 服务器扩展 Claude 可调用的工具

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L1: # tclaude — Claude in the terminal &nbsp;&nbsp;
> L5: Unlike other tools that aim to support all kinds of LLMs, **tclaude** is designed specifically for Claude.
> L22: Then set the `ANTHROPIC_API_KEY` environment variable to your Claude API key and you are good to go.

## 星数曲线

```mermaid
xychart-beta
    title "Tom94/tclaude 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `950ba5d4a970` · [字段定义](../../DATASET.md)*
