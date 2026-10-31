# 147228/dsh-xiaoyao-skins

⭐ 23 · CSS · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/147228/dsh-xiaoyao-skins) · [官网](https://147228.github.io/dsh-xiaoyao-skins/) · 个人维护 · 中文 README

**DeepSeek Harness Web 的社区皮肤合集与一键换肤安装器**

面向 DeepSeek Harness Web profile 的表现层皮肤插件合集：提供六套皮肤，通过 npx 一行命令调用 xiaoyao-skin 安装器经官方 dsh plugin add/remove 接入，支持指定 profile、--dry-run 与恢复官方界面；另带皮肤创建模板与 doctor 检查工具供社区创作。皮肤只做表现层，运行时禁止网络请求与导入功能型 DSH 服务，不改 DSH 源码、不读取会话数据。许可分层：代码 MIT、部分衍生构建支持 BSD-3-Clause、美术素材 CC BY-NC 4.0（禁止商业用途）。需 Node.js 20+ 与已初始化的 DeepSeek Harness。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- npx 一行命令安装/切换/卸载六套皮肤
- 皮肤模板（create）与合集检查工具（doctor）供社区创作
- 皮肤仅表现层：禁止网络请求、不改 DSH 源码、不读会话数据
- pnpm 未预装时经 Corepack/npx 临时提供，不修改全局配置

## 适用场景

- 给自己的 DeepSeek Harness Web 界面一键换肤并随时恢复官方样式
- 按模板创作自定义 DSH 皮肤并用 doctor 校验
- 在多 profile 环境下为不同 profile 安装不同皮肤

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L3: 一套面向真实 DeepSeek Harness Web profile 的社区皮肤合集表现层插件。每套皮肤都是一个可安装、可卸载、可测试的 DSH，不替换会话、模型、工具、沙箱或插件系统；
> L100: 1. 先通过官方 `dsh plugin add` 安装目标皮肤；
> L104: 皮肤本身必须只做表现层工作，运行时禁止发起网络请求，也禁止导入功能型 DSH

## 星数曲线

```mermaid
xychart-beta
    title "147228/dsh-xiaoyao-skins 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `263bc7737219` · [字段定义](../../DATASET.md)*
