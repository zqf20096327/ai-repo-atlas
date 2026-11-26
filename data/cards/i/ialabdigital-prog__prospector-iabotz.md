# ialabdigital-prog/prospector-iabotz

⭐ 10 · Python · MIT · 推送 2026-07-14 · [GitHub](https://github.com/ialabdigital-prog/prospector-iabotz) · [官网](https://ialabdigital.com.br) · 组织维护

**本地商机线索挖掘平台：AI 重建弱数字存在感的商家网站**

基于 Flask 的商业线索（lead）自动化平台：按细分与城市在 Google Maps 搜索商家，结果不足时用 Apify 补充，去重并按可配置 TC 分数筛选；对网站质量差的商家用 LLM 选取创意简报、提取品牌视觉并生成重建站点（KIE 生成配图），发布到带 HTTPS 的子域名，再经 Gmail 草稿与 WhatsApp（Evolution API）发送商业提案，附 Kanban 管道与跟进例程。默认草稿模式，发送需显式授权，发送前有安全锁校验。安装需 git clone 后运行 install.sh，用 gunicorn 与 worker 进程运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Google Maps 按细分/城市搜线索，Apify 自动补足，智能去重
- AI 网站重建：32 种视觉方向、品牌视觉提取、KIE 生成配图、质量门拦截丢失内容的版本
- Gmail（Composio）+ WhatsApp（Evolution API）提案与跟进，默认草稿模式
- Kanban 管道面板、异步任务队列与实时状态

## 适用场景

- 批量发现数字存在感弱的本地商家作为潜在客户
- 为差网站商家自动生成重建站点并附前后对比提案
- 按 Kanban 管道跟进商机并自动执行一次跟进

## 场景标签

`网页抓取` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L17: **Prospector IA Botz** is an open-source commercial prospecting platform that automates the entire **discovery → qu
> L37: ### 🎨 AI-Powered Redesign (LLM + KIE)
> L44: - **KIE MCP image generation**: hero 16:9, support 4:5, detail 1:1

## 星数曲线

```mermaid
xychart-beta
    title "ialabdigital-prog/prospector-iabotz 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-11-26"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-24 10 → 2026-11-26 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `03d1785d5d96` · [字段定义](../../DATASET.md)*
