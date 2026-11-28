# nirvanasangsara-AI/phosphor-hud

⭐ 12 · Swift · MIT · 推送 2026-11-27 · [GitHub](https://github.com/nirvanasangsara-AI/phosphor-hud) · 个人维护

**macOS 悬浮 HUD：汇总多个 AI 编码订阅的用量与限额**

原生 SwiftUI 编写的 macOS 菜单栏与悬浮面板工具，读取本机已安装 AI 编码工具的本地日志、OAuth token 与官方用量接口，汇总显示各订阅额度百分比、重置时间与消耗速率，并据最近采样拟合斜率预测到达上限的时间。还按 API 牌价折算本地日志成本计算订阅 ROI，通过 gh 登录只读统计 GitHub PR 效率。运行需 macOS 14+ 与 Xcode Command Line Tools，不刮取 cookie、不做浏览器自动化，数据全部留在本地。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动检测 30+ 提供商（Claude Code、Codex、Gemini CLI、Grok、Copilot 等）并显示限额与重置时间
- 按最近采样拟合斜率，输出每小时消耗速率与预计触顶时间
- 按 API 牌价折算本地日志成本，计算订阅 ROI 并绘制 14 天图表
- 不刮取 cookie、不打印或存储 token，数据保留在本地

## 适用场景

- 同时订阅多个 AI 编码服务时在一个面板查看各限额与重置时间
- 预测当前用量何时到达上限以安排编码任务
- 按 API 牌价核算各订阅方案的实际使用价值
- 跟踪个人 GitHub PR 合并与提交效率

## 场景标签

 · 领域:开发者工具/用量监控

## 证据(README 行号)

> L4:  Native SwiftUI for macOS. Claude Code, Codex, Google AI, Grok, Copilot and 30+ more. No cookies scraped, ever.
> L26: - **Always on top, natively.** A SwiftUI panel with no web runtime that floats over every Space. Compact mode, opac
> L55: macOS 14+ and the Xcode Command Line Tools. To try it without logging in to anything, run


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `3b7739235ee1` · [字段定义](../../DATASET.md)*
