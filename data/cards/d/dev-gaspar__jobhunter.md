# dev-gaspar/jobhunter

⭐ 14 · Python · MIT · 推送 2026-08-17 · [GitHub](https://github.com/dev-gaspar/jobhunter) · [官网](https://dev-gaspar.github.io/jobhunter/) · 个人维护

**自动化 LinkedIn 求职的 CLI 工具：找岗位、AI 生成简历并发送申请**

面向求职者的 Python CLI 工具，面向任意行业。用 Playwright 持久会话抓取 LinkedIn 帖子，四个 Gemini agent 分别完成岗位过滤、按岗位定制 PDF 简历（ReportLab、4 种模板、ATS 字符规范化）、撰写申请邮件、优化搜索词；经 Gmail SMTP（App Password）自动发送。支持交互式 7 步 setup、人工预览、dry-run、公司黑名单、30 天去重与申请历史。另提供 Windows 免安装依赖的桌面安装包。限制：依赖 LinkedIn 会话与 Gemini API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 个 Gemini agent：过滤、CV 定制、邮件撰写、搜索词优化
- Playwright 持久会话抓取 LinkedIn 并提取招聘者邮箱
- 4 种 PDF 简历模板与 ATS 字符规范化
- dry-run / 预览 / 黑名单 / 去重 / 申请历史

## 适用场景

- 批量扫描 LinkedIn 帖子并筛选真实相关岗位
- 按每个岗位自动生成定制简历与申请邮件
- 维护已投递记录避免 30 天内重复申请

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L178: 6. **CV personalizado**: Otro agente de IA genera un CV en PDF adaptado a cada oferta especifica, reescribiendo tu
> L179: 7. **Email personalizado**: Un tercer agente escribe un email de aplicacion corto, directo, y humano

## 星数曲线

```mermaid
xychart-beta
    title "dev-gaspar/jobhunter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7a5b07650e45` · [字段定义](../../DATASET.md)*
