# yang2020chen/pi-extension-convergence

⭐ 18 · TypeScript · MIT · 推送 2026-09-21 · [GitHub](https://github.com/yang2020chen/pi-extension-convergence) · 个人维护 · 中文 README

**Pi Coding Agent 的收敛引导扩展：抑制复测死循环与超时**

面向 Pi Coding Agent 的 TypeScript 扩展，针对深度推理模型（Bonsai 2、Qwen 2.5/3、DeepSeek R1）的过度复测与思维震荡问题，通过 Pi 官方 Extension API 拦截 tool_call/tool_result，在证据充分时以 steer 消息提醒模型收敛。采用双梯级引导（强证据 steer 与同测试 3 次通过防死循环）、证据过滤（/health、sqlite3、ls/read/grep 不计入）与源码修改后自动解锁再引导的机制，不杀进程。安装方式为放置单文件 convergence.ts 到项目或全局扩展目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双梯级 Steering：多维强证据引导 + 同测试 3 次通过的防死循环兜底
- 严格证据过滤：/health、sqlite3、ls/read/grep 不计入完成证据
- 源码修改后自动清空证据并解锁，可再次引导
- 通过 Pi 官方 Extension API 运行，不杀进程、不改工作区状态

## 适用场景

- 深度推理模型编码 Agent 频繁复测导致步数超时的场景
- 希望以软引导而非强杀进程方式让 Agent 收敛交卷
- 为 Pi Coding Agent 增加基于测试证据的任务完成判定

## 场景标签

 · 领域:开发者工具/Agent 基础设施

## 证据(README 行号)

> L7: > **Production-grade Convergence & Anti-Overthinking Steering Extension for Pi Coding Agent.**
> L25: Unlike naive supervisors that violently kill processes (`SIGKILL`) or blindly intercept bash commands, `pi-extensio

## 星数曲线

```mermaid
xychart-beta
    title "yang2020chen/pi-extension-convergence 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-26 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f36ae5e001bc` · [字段定义](../../DATASET.md)*
