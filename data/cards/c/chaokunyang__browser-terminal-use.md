# chaokunyang/browser-terminal-use

⭐ 26 · JavaScript · Apache-2.0 · 推送 2026-03-31 · [GitHub](https://github.com/chaokunyang/browser-terminal-use) · 个人维护 · 中文 README

**把浏览器/云终端变为本地 AI Agent 可脚本化执行命令的桥接工具**

由 Chrome MV3 扩展、本地 WebSocket 守护进程 browterm-daemon（默认 ws://127.0.0.1:17373）与 browterm CLI 三部分组成：CLI 发送 exec 请求，守护进程排队认证并用唯一 marker 包装命令，扩展将其注入已绑定的浏览器终端页执行，回传流式输出与哨兵标记提取的退出码，CLI 以相同返回码退出。面向运行本地 LLM Agent 循环、需在云端浏览器终端（如云 GPU、容器集群、堡垒机网络）远程执行并审计命令的用户。要求 macOS、Node.js 20+ 与 Chrome；不支持完全交互式 TUI，部分终端 websocket 编码专有可能导致解析失败。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- marker 包装命令实现退出码捕获与流式输出回传
- 守护进程串行队列、服务端超时与 cancel 语义
- 优先 Chrome Debugger API 注入，websocket 优先捕获、DOM 回退
- 提供 JSON 输出模式与 token 认证选项

## 适用场景

- 本地 Agent 循环在云端浏览器终端执行命令并取回可验证输出与退出码
- 在堡垒机/容器集群等远程环境做 AI 辅助调试
- 本地自动化脚本以命令方式驱动网页终端

## 场景标签

 · 领域:开发者工具/Agent 基础设施

## 证据(README 行号)

> L5: Chrome extension + local daemon + CLI for executing commands in a browser-hosted terminal and returning structured o
> L11: - Agent-first workflow: run local LLM Agent loops, but execute commands in cloud browser terminals.

## 星数曲线

```mermaid
xychart-beta
    title "chaokunyang/browser-terminal-use 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `17a4bfda923d` · [字段定义](../../DATASET.md)*
