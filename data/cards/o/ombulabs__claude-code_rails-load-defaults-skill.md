# ombulabs/claude-code_rails-load-defaults-skill

⭐ 19 · Ruby · MIT · 推送 2026-08-20 · [GitHub](https://github.com/ombulabs/claude-code_rails-load-defaults-skill) · [官网](https://www.fastruby.io/blog/open-source-claude-code-skill-for-rails-upgrades.html) · 组织维护

**帮助 Rails 应用逐步升级 load_defaults 的 Claude Code 技能**

面向 Claude Code 的插件（skill）：检测 Rails 应用当前 load_defaults 版本与 Rails 版本差，从模板生成 new_framework_defaults_X_Y.rb 初始化文件，按风险分级（三级 tier）逐项处理配置——grep 代码库给出建议值、逐条取消注释并等待用户测试提交，最后删除初始化文件、更新 load_defaults 并为保留旧行为的配置写入显式覆盖。覆盖 5.0 至 8.1 的版本迁移，支持插件市场与手动安装。由 FastRuby.io 团队维护。

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

- 检测 load_defaults 与 Rails 版本差异并生成框架默认值初始化文件
- 配置按三级风险分层（Tier 1/2/3），从安全到高风险逐项处理
- 每项配置提供代码库 grep 查找、决策树与风险评估
- 完成后整合：删除初始化文件、更新 load_defaults、为旧值写显式覆盖

## 适用场景

- 我想把 Rails 应用的 load_defaults 逐版本升到与 Rails 版本一致
- 升级框架默认值时希望逐项确认并测试提交，降低破坏风险
- 升级完成后清理初始化文件并保留必要的旧配置覆盖

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: A Claude Code skill that incrementally upgrades `config.load_defaults` in Rails applications by walking through each
> L7: This skill automates the process of bringing a Rails app's `load_defaults` configuration up to match its Rails versi
> L12: - **Iterative Walkthrough**: Uncomments one config at a time, waits for you to test/commit

## 星数曲线

```mermaid
xychart-beta
    title "ombulabs/claude-code_rails-load-defaults-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `93aa84b719fb` · [字段定义](../../DATASET.md)*
