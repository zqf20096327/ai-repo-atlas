# anxuanzi/bua

⭐ 85 · Go · MIT · 推送 2026-01-04 · [GitHub](https://github.com/anxuanzi/bua) · 个人维护

**Go 语言的 AI 浏览器自动化代理库：自然语言驱动网页操作**

面向 Go 开发者的浏览器自动化代理库：通过自然语言描述任务，由 Gemini 驱动的代理观察页面（含截图视觉理解）并自动执行点击、输入、滚动、多标签页等 20+ 浏览器操作，替代基于 CSS 选择器的传统脚本。基于 go-rod 直连 Chrome DevTools Protocol，内置反检测措施、会话持久化、敏感信息日志脱敏，以及从 Fast 到 Max 的五种 token/截图预设。需要 Chrome/Chromium 与 Gemini API Key，目前仅支持 Gemini（经 Google ADK），其他模型支持未提供。

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

- 自然语言驱动 20+ 浏览器自动化工具（导航/交互/标签页/JS 执行）
- 视觉模式默认开启，LLM 分析截图理解页面
- 内置反检测（指纹伪装、拟人鼠标移动、随机延迟）
- 五种预设调节 token 与截图分辨率以平衡成本与能力

## 适用场景

- 用自然语言完成表单填写、电商比价、多步网页工作流
- 免选择器的数据抓取与跨站信息收集
- 用自然语言描述用户旅程做端到端测试
- 监控价格、库存与页面内容变化

## 场景标签

`浏览器自动化` `Agent 框架` `网页抓取` · 领域:Agent 开发

## 证据(README 行号)

> L1: BUA - Browser Use Agent for Go
> L24: result, _ := agent.Run(ctx, "Go to Amazon and find the best-rated wireless headphones under $100")
> L52: go get github.com/anxuanzi/bua

## 星数曲线

```mermaid
xychart-beta
    title "anxuanzi/bua 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 84 --> 86
    line [85, 85]
```

2026-10-18 85 → 2026-10-28 85（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `83c3112f0e93` · [字段定义](../../DATASET.md)*
