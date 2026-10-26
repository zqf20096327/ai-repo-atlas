# idan-rubin/browserclaw

⭐ 82 · TypeScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/idan-rubin/browserclaw) · 个人维护

**面向 AI agent 的浏览器自动化库：快照+编号 ref 精准定位**

基于 Playwright 的 TS/Node 浏览器自动化库，供已有 agent 循环调用：snapshot() 生成带编号 ref（e1、e2…）的文本树，模型读文本返回 ref，库将 ref 解析为 Playwright locator 并执行操作。库本身不调用 LLM、不做决策，可搭配任意模型（示例给出 Anthropic 接线）。附带 Cloudflare/CAPTCHA 挑战检测、隔离配置、陈旧锁恢复与默认拦截私网地址的 SSRF 策略。限制：refs 随页面变化失效需重新快照；CAPTCHA 仅检测不破解。

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

- snapshot+ref 定位：无需 CSS/XPath/视觉模型，一个 ref 对应一个元素
- 库内不做模型调用，agent 循环由调用方拥有
- 内置 Cloudflare/hCaptcha/reCAPTCHA/Turnstile 等挑战检测
- 默认 SSRF 防护：拦截私网、环回与云元数据地址

## 适用场景

- 为自有 LLM agent 循环提供浏览器操作原语
- 用文本快照替代截图降低 token 消耗并保持定位确定性
- 在 Docker/CI 中驱动本机 Chrome 做自动化任务

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L11: The AI-native browser automation library — born from OpenClaw, built on Playwright, embeddable in any TS/Node agent
> L15: browserclaw is just the eyes and hands. Call `snapshot()` and get an AI-readable text tree where every interactive 
> L26: browserclaw never calls an LLM or decides anything; you do. The whole integration is snapshot in, ref out, act — he

## 星数曲线

```mermaid
xychart-beta
    title "idan-rubin/browserclaw 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 80 --> 83
    line [81, 82, 82]
```

2026-10-18 81 → 2026-10-26 82（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b7264a68038e` · [字段定义](../../DATASET.md)*
