# udecode/dotai

⭐ 1,163 · JavaScript · 推送 2026-11-23 · [GitHub](https://github.com/udecode/dotai) · 组织维护

**面向 AI agent 的共享技能集合，覆盖测试审计与 pstack 同步**

dotai 是一组供 agent 使用的共享技能（skills）仓库，内容来自 pstack 插件未覆盖的部分：测试审计（test-audit）、截图走查与视频转录、pstack 的安装/同步/技能漂移审计（sync-pstack），以及无人值守 1Password 登录与 New-Machine 设置的 passwords 技能。工程方法依赖 pstack 插件且不自行 vendor 上游技能，通过 SKILLS.md 记录生成的清单、能力边界与上游技能的固定安装命令，并提供 validate-skills 与 build-workflow 脚本做校验与重建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- test-audit/sync-pstack/passwords 等可安装的共享 agent 技能
- npx skills add 命令按技能与 agent 指定安装
- validate-skills 按 frontmatter 与变更可达性选择性运行技能测试
- build-workflow 重建 SKILLS.md 与 workflow-manifest.json，含重复所有权检查与校验和

## 适用场景

- 为 codex/claude-code 等 agent 安装项目级或全局技能
- 在多个项目中保持 pstack 插件配置一致
- 审计仓库测试质量并生成截图/视频走查材料

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: Shared skills that the pstack plugin does not cover: test audits (`test-audit`, adapted from openclaw's), screenshot
> L22: Install a skill with the Skills CLI, naming the skill and each agent, for example `npx skills add udecode/dotai --s

## 星数曲线

```mermaid
xychart-beta
    title "udecode/dotai 星数(近 8 点)"
    x-axis ["2026-10-23", "2026-10-30", "2026-11-06", "2026-11-08", "2026-11-12", "2026-11-15", "2026-11-21", "2026-11-25"]
    y-axis "stars" 1157 --> 1165
    line [1158, 1161, 1158, 1164, 1163, 1164, 1163, 1163]
```

2026-10-23 1,158 → 2026-11-25 1,163（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `504d79a00c52` · [字段定义](../../DATASET.md)*
