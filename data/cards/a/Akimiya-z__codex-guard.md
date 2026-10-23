# Akimiya-z/codex-guard

⭐ 133 · JavaScript · MIT · 推送 2026-10-15 · [GitHub](https://github.com/Akimiya-z/codex-guard) · [官网](https://akimiya-z.github.io/codex-guard/) · 个人维护

**拦截 AI 生成 PR 常见问题的 GitHub Actions 质量门禁**

面向使用 AI 编码代理团队的 GitHub Actions 工作流检查：通过标签、分支前缀或标题识别疑似代理生成的 PR，对新增行扫描 TODO/FIXME 等残留标记与硬编码密钥（AWS/GitHub/OpenAI 等，报告中脱敏），校验提交信息是否符合约定式提交，并读取 commit statuses 与 check runs 判定 head 提交 CI 状态；发现项以 check-run 注解定位到文件行并附 PR 摘要评论。提供 observe/balanced/strict 三档预设、仓库级 YAML 策略覆盖、本地 CLI 干跑（npx codex-guard）与供代理提交前自检的 skill 包。默认仅门禁代理 PR，人写 PR 不受影响。

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

## 能力要点

- 四类检查：TODO 标记、密钥扫描、提交信息规范、head 提交 CI 状态
- 按标签/分支前缀/标题识别代理 PR，默认不门禁人写 PR
- observe/balanced/strict 三档预设 + 仓库级 YAML 策略覆盖
- 本地 CLI 干跑与 Codex/Claude Code 提交前自检 skill

## 适用场景

- 阻止 AI 代理 PR 携带 TODO 残留或泄露密钥进入 main
- 统一团队 AI 生成 PR 的提交信息与 CI 绿灯标准
- 让代理在提交前本地自检，减少 CI 门禁拦截

## 场景标签

`代码审查` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L13: **An automatic quality gate for AI-generated pull requests.** Stop TODO leftovers,
> L42: Codex Guard runs on `pull_request`, figures out whether the PR looks
> L135: By default Codex Guard **only gates PRs it believes were written by an agent**,

## 星数曲线

```mermaid
xychart-beta
    title "Akimiya-z/codex-guard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 132 --> 137
    line [136, 133]
```

2026-10-18 136 → 2026-10-23 133（-3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `4091281d04d5` · [字段定义](../../DATASET.md)*
