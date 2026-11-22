# elizaOS/eliza

⭐ 19,910 · Java · MIT · 推送 2026-11-21 · [GitHub](https://github.com/elizaOS/eliza) · [官网](https://elizaresearch.ai/) · 组织维护

**给开发者的开源 agent 操作系统规范与工具链**

本仓库给出 Eliza v4 on Vibestack 的规格说明：涵盖内核、agent 宿主、设备镜像、云服务（身份、计费、模型接入）与助手插件；agent 在设备端运行，云端提供身份、计费与模型访问。规格包含需求、Quint 模型及 VibeLang 与 Effect 实现的生成契约。开发流程为 pnpm 安装后通过 gen/check/verify 生成契约、检查模型轨迹与重放、证明安全义务；另含 Android Keystore 密码恢复测试夹具的构建与运行步骤。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 1.1 天,年发版 17,159 位贡献者
- 涨星:近 1 天 **+2**(自 20261016 起算)
- 下载:GitHub Release 附件 累计 144,967(17 个 release)
- 平台:LINUX / ANDROID / WEB · 协议:—

## 能力要点

- 规格化覆盖内核、agent 宿主、设备镜像、云服务与插件
- pnpm check 生成契约、检查模型轨迹与重放并证明安全义务
- 基于 Quint 形式化模型与生成的 VibeLang/Effect 契约
- 提供 Android Keystore 密码备份/恢复的双设备测试夹具

## 适用场景

- 按规格构建与验证 Eliza agent 内核实现
- 审查 agent 平台的安全义务证明与模型轨迹
- 测试 Android 设备上的密码保管库备份与恢复流程

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: This workspace specifies Eliza v4 on Vibestack: the kernel, the agent host,
> L5: on the device; the cloud serves identity, billing and model access. The

## 星数曲线

```mermaid
xychart-beta
    title "elizaOS/eliza 星数(近 25 点)"
    x-axis ["2026-10-20", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-22"]
    y-axis "stars" 19598 --> 19938
    line [19626, 19635, 19638, 19640, 19644, 19652, 19654, 19672, 19698, 19714, 19736, 19744, 19748, 19644, 19792, 19834, 19848, 19864, 19873, 19882, 19886, 19900, 19903, 19907, 19910]
```

2026-10-20 19,626 → 2026-11-22 19,910（+284）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 low · 依据 README sha `93d630f6b2b7` · [字段定义](../../DATASET.md)*
