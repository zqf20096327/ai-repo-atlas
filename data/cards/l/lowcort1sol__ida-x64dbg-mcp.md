# lowcort1sol/ida-x64dbg-mcp

⭐ 15 · Python · MIT · 推送 2026-05-21 · [GitHub](https://github.com/lowcort1sol/ida-x64dbg-mcp) · 个人维护

**连接 Codex 等 AI agent 与 IDA Pro/x64dbg 的本地 MCP 逆向工程平台**

面向逆向工程开发者的本地优先 MCP 平台：通过 stdio 薄适配器把 Codex 等 AI agent 接入自建守护进程，IDA Pro 9.1（IDAPython 桥）与 x64dbg x64（C++ 插件桥）经 127.0.0.1 WebSocket 连接，实现静态/动态分析地址实时同步。守护进程用 SQLite+JSONL 持久化会话，提供上下文预算档位、语义缓存、策略门控的补丁规划（备份/diff/回滚）与恶意软件分析工作区。自述为 alpha 原型：Windows 优先、x64 优先、单活动会话，含 100 项自动化测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- IDA 静态分析与 x64dbg 动态调试在同一会话中地址映射与实时同步
- 上下文预算档位（quick/compact/deep/forensic）与语义缓存控制 AI 上下文用量
- 策略门控的补丁规划与文件打补丁（备份/字节级 diff/回滚），默认 analysis-safe 模式
- 恶意软件分析工作区：样本哈希、IoC、提取配置、行为报告与 JSON/Markdown/HTML 导出

## 适用场景

- 让 AI agent 在调试器断点处结合 IDA 伪代码解释当前函数
- 通过 workflow 组合工具定位密码校验逻辑并规划补丁
- 整理恶意软件样本的分诊、IoC 与行为报告
- 把运行时地址映射回 IDA 并回写注释/重命名建议

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: IX64MCP connects an AI agent such as Codex to a live reverse-engineering workspace: IDA Pro for static analysis, x64
> L31: - Codex talks to a thin MCP adapter over stdio.
> L33: - IDA and x64dbg connect to the daemon over `127.0.0.1` WebSocket bridges.

## 星数曲线

```mermaid
xychart-beta
    title "lowcort1sol/ida-x64dbg-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `a2d75ab235cb` · [字段定义](../../DATASET.md)*
