# interfere-inc/landmines

⭐ 698 · TypeScript · MIT · 推送 2026-11-18 · [GitHub](https://github.com/interfere-inc/landmines) · [官网](https://www.npmjs.com/package/@interfere/landmines) · 组织维护

**约束 AI 生成代码诚实性的 Oxlint 规则集**

面向 Oxlint 的 lint 插件包，针对编码 agent 为通过 CI 而采取的取巧行为提供静态检查规则：禁止测试中的模块 mock、固定 sleep、轮询竞态、重试掩盖 flake、抬高超时；另含风格（禁散文注释）、结构（测试同置、测试文件命名、显式导出）与类型（禁显式返回类型）四类插件。每条规则失败时给出替代做法提示，部分规则支持按文件精确计数的 allowlist 以便渐进采用。要求 Oxlint 1.81+ 与 Node 22.18+，通过 bun/npm 安装后在 .oxlintrc.json 中扩展推荐配置使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- testing 规则禁止 mock/stub、固定 sleep、竞态轮询、重试与超时掩盖
- 规则支持按文件精确计数的 allowlist，且违规少于配额时报错以便收紧
- 四个插件分组：testing/style/structure/types
- 每条 lint 报错附带应采取的替代做法说明

## 适用场景

- 在 CI 中拦截编码 agent 用 mock 或 sleep 糊弄测试的代码
- 渐进治理存量代码库中的 flaky 测试
- 约束 AI 生成代码的注释、测试组织与导出规范

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: Oxlint rules that keep AI-written code honest.
> L5: Coding agents are fast, and they optimise for green checks. Left alone, they

## 星数曲线

```mermaid
xychart-beta
    title "interfere-inc/landmines 星数(近 8 点)"
    x-axis ["2026-10-30", "2026-11-10", "2026-11-12", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22"]
    y-axis "stars" 0 --> 767
    line [4, 5, 6, 45, 569, 680, 696, 698]
```

2026-10-30 4 → 2026-11-22 698（+694）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `dc668dea8d3b` · [字段定义](../../DATASET.md)*
