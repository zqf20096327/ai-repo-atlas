# dinoDanic/diny

⭐ 132 · Go · MIT · 推送 2026-05-12 · [GitHub](https://github.com/dinoDanic/diny) · [官网](https://diny.run) · 个人维护

**从暂存 diff 生成 git 提交信息的 CLI，无需 API key**

Go 编写的开源终端工具：读取 `git diff` 暂存变更，过滤 lockfile、二进制与构建产物等噪声文件，一次生成 3 条候选提交信息，支持内联编辑或调用 $EDITOR 修改。交互式 TUI 覆盖提交、配置、changelog、时间线等场景，另可将暂存变更按关注点拆分为多个提交。声明无需 API key 与注册。安装途径包括 brew、Scoop 与 GitHub Releases 预编译二进制，支持与 git alias 和 LazyGit 集成，采用 MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取暂存 diff 生成 3 条候选提交信息，自动过滤 lockfile/二进制/构建产物
- 按关注点将暂存变更拆分为多个提交
- AI 驱动的 tag/commit 间 changelog 生成与提交历史时间线分析
- 三层配置系统（全局/项目共享/项目私有），10+ 主题

## 适用场景

- 我不擅长写提交信息，想让工具根据代码变更自动生成
- 一次暂存了太多改动，想按关注点拆成多个提交
- 想在发布时自动生成两个版本之间的 changelog

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5: **Free AI git commit messages. No API key. No signup.**
> L13: - Generates 3 message variants; inline editing or open in `$EDITOR`

## 星数曲线

```mermaid
xychart-beta
    title "dinoDanic/diny 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 130 --> 133
    line [131, 132, 132]
```

2026-10-18 131 → 2026-10-31 132（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `cc2e0d12069e` · [字段定义](../../DATASET.md)*
