# verne-build/verne

⭐ 15 · TypeScript · GPL-3.0 · 推送 2026-09-02 · [GitHub](https://github.com/verne-build/verne) · [官网](https://verne.build) · 组织维护

**面向 CLI 编码 agent 的本地开源 IDE 工作区**

Verne 是一款在本地运行的 agent 工作区应用：以终端中的 CLI agent 为中心，集成文件编辑器（基于 Monaco 与 LSP）、逐行 diff 审查与 git 提交、可由 agent 经 MCP 驱动的浏览器标签页、供 agent 读取的工作区笔记，以及基于 sherpa-onnx 的设备端语音输入。分离式守护进程持有 PTY，使终端会话在应用退出或重启后仍可重连。agent 使用用户自行安装与登录的账号（如 Claude Pro/Max），代码不离开本机。目前仅提供 macOS（Apple Silicon 与 Intel）版本，Linux 与 Windows 在路线图中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个终端带实时状态点，识别 agent 工作/等待/完成状态
- 分离式守护进程持有 PTY，会话跨应用重启存活
- 内置 Monaco 编辑器与 LSP，diff 审查与提交在同一窗口完成
- 浏览器与工作区笔记经 MCP 暴露给 agent 使用

## 适用场景

- 在统一工作区中运行并监控多个 CLI 编码 agent
- 审查 agent 修改的文件并逐行查看 diff 后提交
- 让 agent 在内置浏览器中验证其工作成果
- 重启或断开后重新接入仍在运行的 agent 会话

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L13: Your agents run in a terminal. The files they touch, the diffs you review, the browser you verify in, and the conte
> L15: - **Your agents, your accounts.** Verne runs the CLI agents you installed, signed in with your own accounts. On a C
> L23: Any CLI agent runs in a Verne terminal; the ones above also show their live status.

## 星数曲线

```mermaid
xychart-beta
    title "verne-build/verne 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `79b872277ad3` · [字段定义](../../DATASET.md)*
