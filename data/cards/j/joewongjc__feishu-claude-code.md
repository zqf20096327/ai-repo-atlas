# joewongjc/feishu-claude-code

⭐ 169 · Python · MIT · 推送 2026-04-14 · [GitHub](https://github.com/joewongjc/feishu-claude-code) · 个人维护 · 中文 README

**把本机 Claude Code CLI 桥接到飞书的 WebSocket 客户端**

在飞书/本地 Claude Code CLI 之间建立 WebSocket 长连接的桥接服务：飞书消息经本机 main.py 以 subprocess 调用 claude CLI（stream-json 模式），解析事件流后通过飞书卡片 PATCH API 流式更新输出。复用 Claude Max/Pro 订阅，无需 API Key 与公网 IP。支持跨设备 session 管理、群聊隔离、交互式按钮、图片识别、Skills 透传与看门狗重启。面向使用 Claude Code 的开发者，需 Python 3.11+、Claude Code CLI 与自建飞书应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WebSocket 长连接桥接飞书与本机 claude CLI，流式卡片输出
- 跨设备 session：/resume 恢复、CLI Handover 终端会话移交飞书
- 群聊支持：@机器人触发、每群独立 session/模型/工作目录
- 复用 Claude Max/Pro 订阅，无需 API Key 与公网 IP

## 适用场景

- 在手机飞书里随时对本机 Claude Code 会话做 code review 和 debug
- 终端调试到一半，出门后用手机继续同一会话
- 多项目多群并行为不同代码库绑定 Claude Code 工作目录

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: 在飞书里直接和你本机的 Claude Code 对话。
> L135: │  飞书 App │◄───────────►│ feishu-claude  │─────────────►│ claude CLI │
> L143: 2. 调用 `claude` CLI 的 `--print --output-format stream-json` 模式

## 星数曲线

```mermaid
xychart-beta
    title "joewongjc/feishu-claude-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 168 --> 170
    line [169, 169]
```

2026-10-18 169 → 2026-10-23 169（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `97ffc4b362aa` · [字段定义](../../DATASET.md)*
