# Raynan00/shoal

⭐ 14 · TypeScript · MIT · 推送 2026-08-18 · [GitHub](https://github.com/Raynan00/shoal) · 个人维护

**用 AI 用户群体在真实浏览器中测试网站、生成摩擦地图的工具**

面向 Web 产品 QA/UX 测试的 Node.js 工具：向一个 URL 释放一组人设驱动的 agent（Claude computer use + Playwright），每个 agent 在独立 Chromium 里以截图-决策-行动循环执行任务，实时上报问题；结束后输出按命中 agent 数排名的摩擦地图。支持 9 种人设 × 7 种策略、多用户交互场景（marketplace/flash-sale 等，可扩展到约 1000 参与者）、并发竞态模式与 Claude 复核确认机制。另提供无 API key 的脚本化 demo 模式，实时仪表盘以像素风水族箱可视化漏斗。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- persona 驱动的 agent 群在真实 Chromium 浏览器中执行任务并实时上报 findings
- 摩擦地图：按命中 agent 数对问题聚类排名
- 多用户交互场景（买卖双方、秒杀并发等），可扩展到约 1000 参与者，结果经服务端核验
- 支持 anthropic / subscription / openai 三类 provider，verify pass 用 Claude 复核每条 finding

## 适用场景

- 上线前让一组 AI 用户跑完整购买/注册流程，找 UX 断点
- 用千级并发买家场景验证库存扣减是否存在超卖竞态
- 让不同人设（急躁型、只读屏幕阅读器用户等）测试产品可达性与易用性

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L8: the page as pixels (Claude computer use + Playwright), attempts the task in character,
> L48: ## Quick start — the 60-second demo (no API key)
> L133: Each agent runs a Claude computer-use loop

## 星数曲线

```mermaid
xychart-beta
    title "Raynan00/shoal 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a34b520ef489` · [字段定义](../../DATASET.md)*
