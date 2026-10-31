# nicolasmaldonadoj/google-ads-cli-toolkit

⭐ 20 · Python · MIT · 推送 2026-05-06 · [GitHub](https://github.com/nicolasmaldonadoj/google-ads-cli-toolkit) · 个人维护

**用终端脚本和 Claude Code 接管自己 Google Ads 账户的开源工具包**

面向在 Google Ads 投放、依赖第三方代运营的广告主与小团队：打包一组 Python 脚本，通过 Google Ads API 直接审计、诊断和批量修改账户（关键词、出价策略、转化操作等），并提供 GTM、GA4 的同等模式。设计为与 Claude Code 配合使用：用户用西班牙语对话，agent 读取 CLAUDE.md playbook 并代为执行命令；也可按 docs/SETUP.md 手动运行。含 6 步 OAuth/Developer Token 设置流程；审计脚本只读，示例脚本会改账户并带占位符守卫。100% 本地运行，直接调用 Google 官方 API。MIT 许可。

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

- Python 脚本经 Google Ads API 审计与批量修改账户（审计脚本只读）
- CLAUDE.md playbook 让 Claude Code 代读 repo、写并执行命令
- 覆盖 GTM 与 GA4 的迁移/审计同等模式及常见修复手册
- 100% 本地运行，不收集数据，示例脚本带未配置即中止的守卫

## 适用场景

- 与代理商/自由职业者结束合作后收回并审计自己的 Google Ads 账户
- 无 PPC 专家的小团队自己排查账户出价、关键词与转化配置
- 把 GTM 容器和 GA4 资源迁回自己名下的 Google 账号

## 场景标签

 · 领域:数字营销/广告运维

## 证据(README 行号)

> L7: trabajar de la mano con Claude Code (u
> L31: herramientas programáticas para que tú — con la ayuda de Claude Code —
> L81: Si prefieres hacerlo manualmente, sigue docs/SETUP.md.

## 星数曲线

```mermaid
xychart-beta
    title "nicolasmaldonadoj/google-ads-cli-toolkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `1c10453cf426` · [字段定义](../../DATASET.md)*
