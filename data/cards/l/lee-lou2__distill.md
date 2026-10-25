# lee-lou2/distill

⭐ 34 · Rust · 推送 2025-12-24 · [GitHub](https://github.com/lee-lou2/distill) · 个人维护

**Rust 网页抓取 API 服务器，可选 Gemini 做内容分析**

基于 Axum/Tokio 与 headless_chrome 的 REST API 服务器：抓取 JavaScript 渲染页面，输出 HTML 或 Markdown，自动提取标题与 Open Graph 标签；可选传入 prompt 与 Structured Output schema，调用 Gemini API 对页面内容做结构化分析，分析失败时仍返回抓取结果。支持 API key 认证、最多 50 个并发请求（Docker 内默认 10）、标签页复用与自动清理。提供 cargo run 本地运行与 Docker 镜像（内含 Chromium，约 450MB）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Headless Chrome 抓取 JS 渲染页面，输出 Markdown/HTML
- 可选 Gemini Structured Output 内容分析，失败不影响抓取结果
- 50 并发、标签页复用与 10 秒页面超时等性能参数
- API key 认证与 CORS 控制环境变量

## 适用场景

- 抓取动态渲染网页并转成 Markdown 供下游使用
- 在抓取流程中附带结构化 LLM 分析（如抽取字段）
- 以 Docker 部署一个内部抓取+分析 API 服务

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L9: Distill은 웹 페이지를 스크래핑하고, 선택적으로 LLM(Gemini)을 통해 콘텐츠를 분석하는 REST API 서버입니다.
> L13: - **웹 스크래핑**: Headless Chrome으로 JavaScript 렌더링된 페이지 지원
> L16: - **LLM 분석**: Gemini API를 통한 구조화된 콘텐츠 분석

## 星数曲线

```mermaid
xychart-beta
    title "lee-lou2/distill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-25 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4a886cbd9e1b` · [字段定义](../../DATASET.md)*
