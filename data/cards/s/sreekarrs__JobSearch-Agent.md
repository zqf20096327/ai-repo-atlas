# sreekarrs/JobSearch-Agent

⭐ 65 · Python · GPL-3.0 · 推送 2026-01-19 · [GitHub](https://github.com/sreekarrs/JobSearch-Agent) · 个人维护

**求职者自动化求职工具：LinkedIn 抓取+AI 生成简历与求职信**

基于 Python 3.10+ 的求职自动化系统：用 Playwright 抓取 LinkedIn 职位数据（职位描述、公司信息、招聘团队），带匿名化（随机 UA、时区、WebGL/Canvas/WebRTC 屏蔽）、HTTP/SOCKS5 代理与限速保护；通过 Gemini API key 调用 AI 生成定制简历与求职信。提供同步/异步双模式流水线，SQLite 存储与去重，含 CLI 与 FastAPI 服务器（REST/WebSocket）。另附 BugMeNot 凭据抓取器。声明仅供教育和个人使用，需遵守 LinkedIn 服务条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Playwright LinkedIn 抓取：多浏览器、匿名化、代理与限速保护
- AI 生成 CV 与求职信（Gemini API）
- 同步/异步统一流水线，SQLite 存储与自动去重
- FastAPI 服务器提供 REST/WebSocket 接口

## 适用场景

- 批量抓取并结构化保存 LinkedIn 职位信息
- 按目标职位自动生成定制简历与求职信
- 通过 API 或 CLI 集成到自己的求职流程

## 场景标签

`网页抓取` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L13: An intelligent job search automation system with **LinkedIn scraping**, **AI-powered CV generation**, and **cover l
> L36: GOOGLE_API_KEY=your_gemini_api_key

## 星数曲线

```mermaid
xychart-beta
    title "sreekarrs/JobSearch-Agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 63 --> 66
    line [64, 65, 65]
```

2026-10-18 64 → 2026-10-28 65（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `2d2180dde2f4` · [字段定义](../../DATASET.md)*
