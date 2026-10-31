# DITlieD/ELAI-archive

⭐ 24 · Rust · MIT · 推送 2026-10-21 · [GitHub](https://github.com/DITlieD/ELAI-archive) · 个人维护

**已暂停的本地优先 LLM agent 框架研究代码档案**

个人维护的研究档案仓库：探索本地优先、模型无关的 agent 框架（harness），设计上由软件层持有规划、状态、权限、执行、证据与完成判定，模型仅提议动作。仓库含 Rust/Python/Tauri 源码、基准测试与历史结果、659 条计划单元目录和 883 条历史提交（经隐私编辑）。README 明确声明构建可行性与端到端行为未验证，不构成可用产品；作者计划在停更后重启开发，但未给出发布时间。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 模型提议动作、框架层持有规划/权限/验证/完成判定的设计
- 保留 Rust/Python/Tauri 源码、基准测试夹具与历史结果工件
- 归档 883 条历史提交（内容与身份经隐私编辑，日期与父关系保留）
- 提炼五个设计方向：证据外置、fail-closed 验证、日志与重放、有界 worker、代码检索

## 适用场景

- 研究 agent 框架的证据验证与重放机制设计
- 从停更项目中提取可复用的实现片段与设计参考
- 查阅 agent 框架过度工程化的复盘记录

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: ELAI explored a local-first, model-agnostic agent harness: models propose actions,
> L17: work. Retrieval, orchestration, verification, sandboxing, memory, model routing,

## 星数曲线

```mermaid
xychart-beta
    title "DITlieD/ELAI-archive 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c7ba7027a4d7` · [字段定义](../../DATASET.md)*
