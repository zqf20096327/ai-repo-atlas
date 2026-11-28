# Adr1enR1chard/ecologits-extension

⭐ 3 · TypeScript · MPL-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/Adr1enR1chard/ecologits-extension) · 个人维护

**浏览器扩展：逐条估算 ChatGPT/Claude/Gemini 使用的环境足迹**

基于 EcoLogits 的浏览器扩展，在生成式 AI 网页回复下方显示徽章，估算每次回复的能耗、温室气体排放与水资源消耗及区间；弹窗按日/7天/30天/累计统计并按提供商与模型分解，含使用与制造两类影响及 ADEME 日常等价换算。机制上通过包装页面 fetch 读取回复流，按提供商适配器提取模型与文本，用 o200k_base 计数输出 token 后调用 @ecologits/ecologits.js 计算影响。数据仅存浏览器本地，支持 CSV/JSON 导出，支持英语与法语。尚未上架商店，需从源码构建安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 每条回复下方的能耗/温室气体/水足迹徽章与 min–max 区间
- 按日/7天/30天/累计、按提供商与模型分解的统计弹窗
- 低置信估计标注：隐藏推理、未知模型近似、回复被截断
- 数据全部本地存储，可导出 CSV/JSON 或一键删除

## 适用场景

- 统计自己日常使用 ChatGPT/Claude/Gemini 的碳足迹
- 按提供商和模型对比记录各自的环境影响数据
- 导出使用数据用于个人或团队的环境报告

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: Browser extension that estimates the environmental impact of your generative AI usage, reply by reply, powered by Ec
> L33: 3. The background service worker counts the output tokens (`o200k_base` tokenizer), maps the web model to an EcoLog

## 星数曲线

```mermaid
xychart-beta
    title "Adr1enR1chard/ecologits-extension 星数(近 2 点)"
    x-axis ["2026-11-27", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-27 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `93c18595a04b` · [字段定义](../../DATASET.md)*
