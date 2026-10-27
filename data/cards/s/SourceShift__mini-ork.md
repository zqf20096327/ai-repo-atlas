# SourceShift/mini-ork

⭐ 32 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/SourceShift/mini-ork) · [官网](https://miniork.dev) · 个人维护

**面向 AI agent 的验证门控任务运行时，证明修复确实修了 bug**

多模型 agent 运行时：以 kickoff 文件声明目标与成功判据，按 classify→plan→execute→verify→reflect→improve 流程运行 code-fix、docs、refactor-audit 等配方。核心机制是执行证据式验证：verifier 运行测试套件、基线重放与变异充分性检查；certify 命令在 Docker 沙箱中复现 bug 并用生成的恒等式攻击补丁，返回 PROVEN/REFUTED/UNVERIFIED 及 JSON 证书，可接入 CI 门禁。学习环仅保留经验证的教训并注入提示，自我修改有审计与回滚门控，自动 apply 循环默认关闭。项目自述为早期研究级。Python 3.11/3.12，支持 macOS/Linux/WSL，需 Git 与一条模型通道。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- certify 命令：Docker 沙箱中复现 bug、生成恒等式攻击补丁，输出 PROVEN/REFUTED/UNVERIFIED 证书
- 验证链含盲写 spec 测试、基线重放、变异充分性检查，评审模型可否决但不能制造通过
- 学习环仅保留带验证证据的教训，注入账本记录每个节点收到的内容
- 自我修改经 hackability/verifier 审计与非回归门控，保留回滚指针；自动 apply 默认关闭

## 适用场景

- 在 CI 中用 certify 门禁判定 AI 生成的修复是否真实修复 bug
- 以 code-fix 等配方端到端运行经过验证的代码修改工作流
- 为 agent 运行结果提供执行证据与审计记录

## 场景标签

`Agent 框架` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L18: mini-ork turns a goal into a planned, executed, and **verified** run across a fleet of
> L144: `mini-ork certify` takes a change and the bug it claims to fix, reproduces the bug
> L157: so CI can gate on it. Needs Docker and one model lane.

## 星数曲线

```mermaid
xychart-beta
    title "SourceShift/mini-ork 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1ae38e800688` · [字段定义](../../DATASET.md)*
