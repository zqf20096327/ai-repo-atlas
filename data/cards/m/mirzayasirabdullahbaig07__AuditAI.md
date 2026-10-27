# mirzayasirabdullahbaig07/AuditAI

⭐ 46 · Python · 推送 2026-01-31 · [GitHub](https://github.com/mirzayasirabdullahbaig07/AuditAI) · [官网](https://auditai07.streamlit.app/) · 个人维护

**面向网站审计的 Agentic AI Web 应用：SEO/性能/可访问性/安全分析**

基于 Streamlit 构建的 Web 应用：用 BeautifulSoup 与 Requests 抓取并解析目标网站，计算 SEO、性能、可访问性、安全相关指标（加载时间、HTTPS、标题结构、缺 ALT 图片、链接统计等），再将扫描数据发送到 OpenAI 做 agentic 分析，返回问题清单、建议、修复代码片段与优化后 HTML；结果以仪表盘（评分、仪表图/雷达图、词云、热力图）可视化，支持一键下载优化 HTML。需 Python 3.9+ 与 OpenAI API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 扫描页面加载时间、HTTPS、标题结构、缺 ALT 图片等指标
- 调用 OpenAI 生成问题分析、建议、修复片段与优化 HTML
- Streamlit 交互式仪表盘：评分、雷达图、词云、元素热力图
- 一键下载 AI 优化后的网页 HTML

## 适用场景

- 我想快速检查自己网站的 SEO 和性能问题并获得修复建议
- 获取一份可下载的优化后 HTML 用于网页改进
- 通过可视化面板查看网站的审计评分与问题分布

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: An **Agentic AI-powered web application** built with **Streamlit** that audits any website and provides **SEO, perfo
> L74: 3. Scan data is sent to **OpenAI** for agentic analysis.

## 星数曲线

```mermaid
xychart-beta
    title "mirzayasirabdullahbaig07/AuditAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 44 --> 47
    line [45, 46]
```

2026-10-18 45 → 2026-10-27 46（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d5a4ca0468e0` · [字段定义](../../DATASET.md)*
