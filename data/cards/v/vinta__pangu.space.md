# vinta/pangu.space

⭐ 31 · HTML · 推送 2026-10-26 · [GitHub](https://github.com/vinta/pangu.space) · [官网](https://pangu.space) · 个人维护 · 中文 README

**CJK 与西文之间自动加空格的网站与 HTTP API 服务**

基于 pangu.js 的文本加空格服务：在中文、日文、韩文与字母数字符号之间自动插入空格，提供网页（左贴原文、右侧显示加空格结果并高亮差异）与 HTTP API（GET/QUERY/POST）。默认用正则规则处理；对负号与分隔符等歧义符号，可加 feature=ai-spacing 参数由 LLM 判定，每日 AI 配额用尽返回 429。API 对单次请求的歧义符号数量上限为 20 个。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GET/QUERY/POST 三种方式的 /text HTTP API
- 可选 feature=ai-spacing 由 LLM 判定歧义符号的空格
- 网页实时预览并高亮每个新增/删除的空格
- 返回模型逐符号的 candidates 与 label 判定结果

## 适用场景

- 写作或发布前给中英混排文本批量加空格
- 通过 HTTP API 集成到编辑器或发布流程
- 用 AI 模式处理负号等正则难以判定的符号

## 场景标签

 · 领域:文本处理/排版工具

## 证据(README 行号)

> L3: Opinionated paranoid text spacing: automatically inserts whitespace between CJK (Chinese, Japanese, Korean) and ANS 
> L48: Regex rules can't tell a minus sign from a separator, so add `feature=ai-spacing` to the query string and an LLM de

## 星数曲线

```mermaid
xychart-beta
    title "vinta/pangu.space 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-30 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `fd3b6df215ed` · [字段定义](../../DATASET.md)*
