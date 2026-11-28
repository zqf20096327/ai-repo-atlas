# damianvtran/local-operator

⭐ 231 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/damianvtran/local-operator) · [官网](https://local-operator.com) · 个人维护

**在本机托管、监督与连接多个协作 AI agent 的运行时**

Local Operator 是一个运行时，用于在本机承载、监督和连接 agent：单个会话可规划任务、运行工具、浏览并记忆过程；也可作为管理者向受限工具的 worker 委派工作，跨仓库与同级会话互发消息，自行调度后续任务。提供桌面应用（npm 安装）、终端 TUI（uv/pipx/curl 脚本安装）与手机 Web 中继；支持订阅账号登录或 API key 接入多家模型服务，也支持 LM Studio、Ollama、vLLM、llama.cpp 等本地服务器；写入与执行前需用户批准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 托管并监督多个 agent 会话，支持子 agent 并行与角色权限边界（reviewer/coder 等预设角色）
- 跨会话消息（lop send）与多设备点对点 mesh（lop network）
- 订阅账号登录接入 ChatGPT、Claude、Kimi、Grok、Z.AI、Qwen 等，含账号轮换池与模型回退链
- 持久化唤醒调度、后台任务与浏览器扩展驱动 Chrome/Edge/Arc/Brave

## 适用场景

- 在本机组建多 agent 团队并委派开发、评审类任务
- 通过手机或浏览器远程查看与干预 agent 会话
- 复用已有订阅账号运行 agent 而无需逐一申请 API key

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: **Local Operator** is the runtime that hosts, supervises and connects your
> L17: runs on your machine, asks before it writes or executes, draws on the ChatGPT,

## 星数曲线

```mermaid
xychart-beta
    title "damianvtran/local-operator 星数(近 9 点)"
    x-axis ["2026-10-26", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-28"]
    y-axis "stars" 217 --> 232
    line [218, 223, 226, 229, 230, 231, 218, 229, 231]
```

2026-10-26 218 → 2026-11-28 231（+13）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `223b61fdf840` · [字段定义](../../DATASET.md)*
