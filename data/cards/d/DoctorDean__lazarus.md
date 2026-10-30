# DoctorDean/lazarus

⭐ 67 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/DoctorDean/lazarus) · 组织维护

**把废弃科研仓库复活为可调用流水线组件的 agent 工具**

面向科研与计算生物学用户的 CLI agent：给定一个 GitHub 链接，Scout 读取仓库与论文起草复活计划（能力、基础镜像、可证伪 sanity check），随后在一次性容器沙箱中执行 commit 时代依赖钉扎与 build→run→读 traceback→修补循环，产出集成契约（可导入模块、CLI、钉扎容器、冒烟测试），修复以带 CI 的 PR 形式回馈上游。复活产物可通过注册表拉取并用 YAML 组装成流水线，支持本地/远程/GPU 执行。驱动 Claude Agent SDK，自主复活循环需 Python ≥ 3.10 + Docker；以 pip 包发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从裸 GitHub URL 出发的自主复活循环（Scout 起草计划 + 容器沙箱修复）
- 产物统一为集成契约：可导入模块 + CLI + 钉扎容器 + 冒烟测试
- 修复以带 CI 的 maintainer-ready PR 回馈上游
- 注册表内 25 个已复活工具可用 lazarus pull 拉取，YAML 组装跨领域流水线

## 适用场景

- 把无法运行的已发表论文代码恢复为可调用工具
- 复现论文指标并获得 REPRODUCE.md PASS/OFF 证书
- 将多个复活工具组装成如 binder-triage 的科研流水线

## 场景标签

`科研工具` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L29: Lazarus is an agent that **revives** dead research code, lets you **compose** the revivals
> L185: **Auth:** Lazarus drives Claude via the Claude Agent SDK.

## 星数曲线

```mermaid
xychart-beta
    title "DoctorDean/lazarus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-30 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e46b0258e877` · [字段定义](../../DATASET.md)*
