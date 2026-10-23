# aws-samples/sample-specship

⭐ 256 · Shell · MIT · 推送 2026-09-16 · [GitHub](https://github.com/aws-samples/sample-specship) · 组织维护

**Kiro 平台的规格驱动自主工程工作流（侦察→计划→构建→验证→交付）**

以 Kiro Power 形式打包的 AI agent 工程工作流，编排 recon→plan→build→validate→ship 五阶段流水线：棕地代码先做逆向工程产出仓库地图与基线测试，规划阶段含真实网络搜索的市场调研与合同先行验收标准，构建阶段强制 TDD 并按里程碑设置类型检查+测试+构建的硬门，验证阶段由最多 7 个独立对抗验证子代理并行产出带证据的类型化裁决，最终产出可合并的 PR 与交付报告。提供 install.sh 一键安装到 ~/.kiro/steering/，支持 Guided 与全自主两种模式。自述为实验性、未经外部安全审查。

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

- 棕地逆向工程阶段：仓库地图、技术栈、基线测试与保留行为合同
- 最多 7 个对抗验证子代理并行产出带证据的类型化裁决
- 构建里程碑受 typecheck+tests+build 硬门约束，全程 TDD
- 自愈恢复：每个问题一次修复、先写回归测试、最多 3 轮

## 适用场景

- 让 AI agent 端到端完成从需求到 PR 的自主开发
- 在既有代码库上先逆向工程再添加新功能
- 对 AI 生成代码做独立多视角对抗验证

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: A Kiro Power autonomous engineering workflow that orchestrates AI agents through a complete **recon → plan → build →
> L18: |**VALIDATE**|Up to 7 adversarial validators run in parallel as independent subagents, each delegating to its gstac

## 星数曲线

```mermaid
xychart-beta
    title "aws-samples/sample-specship 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 255 --> 257
    line [256, 256]
```

2026-10-18 256 → 2026-10-23 256（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8211005d2537` · [字段定义](../../DATASET.md)*
