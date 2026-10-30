# controlplaneio/sandbox-probe

⭐ 28 · Go · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/controlplaneio/sandbox-probe) · [官网](https://control-plane.io) · 组织维护

**沙箱安全探测工具：审计 AI 编码代理沙箱的实际边界**

单文件静态 Go 二进制，放入沙箱（Claude Code、Gemini CLI、容器等）内部运行，顺序执行任务注册表中的探测任务（读取敏感路径、端口扫描、DNS/网络连通性、Unix socket 与命名管道检测、沙箱运行时指纹识别等），记录内核实际允许的操作并输出一份 JSON 报告。每个 finding 表示探测成功做到某事，缺失即被阻断；支持 seed/cleanup 植入诱饵目标以验证'确实存在可阻断对象'，支持 --config 自定义路径边界策略。面向需评估、调优并持续监控 AI 代理沙箱策略的安全工程师与平台团队，需 Go 1.25+ 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 个 baseline 任务 + 3 个 ps 任务，输出含稳定 finding_type 的 JSON 报告
- 识别 14 种沙箱包装器（Docker/Podman/Landlock/seccomp 等）并区分内核级证实机制
- seed/cleanup 软性植入诱饵（socket/进程），弥补'缺失即阻断'的误读缺口
- 同一二进制可在不同沙箱间生成可直接对比的报告

## 适用场景

- 评估 AI 编码代理被攻陷后能读、写、访问哪些资源
- 为 Landlock/seccomp/容器策略调整提供前后对比证据
- 随代理版本迭代运行探测，告警沙箱边界扩大
- 在不同沙箱间做同口径安全能力对比

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: `sandbox-probe` is a single static Go binary you drop *inside* the sandbox — Claude Code, Gemini CLI, `nono`, a cont
> L15: - **Assessing an AI coding agent's blast radius.** You let developers use Claude Code, Gemini CLI, or similar; you 
> L17: - **Detecting sandbox regressions over time.** Run the probe in your agent's sandbox on every release of the agent 

## 星数曲线

```mermaid
xychart-beta
    title "controlplaneio/sandbox-probe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d7cd0ce07599` · [字段定义](../../DATASET.md)*
