# miskibin/tygodnik-sejmowy

⭐ 18 · TypeScript · NOASSERTION · 推送 2026-10-19 · [GitHub](https://github.com/miskibin/tygodnik-sejmowy) · [官网](http://tygodniksejmowy.pl/) · 个人维护

**波兰议会周报应用：LLM 增强的议会活动数据管道与网页/移动端**

由数据管道与两端应用组成：Python ETL（supagraf）从波兰众议院 API 与 ELI 拉取投票、法案文本、委员会等数据，存入 Supabase，用 DeepSeek LLM 与 qwen3 嵌入做内容增强，并以 DeepSeek 视觉模型读取法案扫描件（回退 tesseract pol）；前端为 Next.js 16 网页，另有 React Native + Expo 移动端，含地图、法案、投票、承诺、民调等视图。面向关注波兰议会活动的用户。采用 PolyForm Noncommercial 许可，商用需另行协议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ETL 管道拉取众议院 API 与 ELI 数据并存入 Supabase
- DeepSeek LLM 与 qwen3 嵌入增强内容，视觉模型读取法案扫描件
- Next.js 16 网页与 Expo 移动端共享 Supabase 后端（只读匿名 key）
- 仓库内置 Claude Code 技能描述波兰立法流程

## 适用场景

- 每周了解波兰议会的投票、法案与委员会动态
- 通过网页地图与移动端浏览法案详情
- 追踪议会承诺与民调数据

## 场景标签

 · 领域:公民科技/议会数据

## 证据(README 行号)

> L6: Otwarty pipeline danych + aplikacje webowa i mobilna, które pobierają dane z Sejmu i ELI,
> L21: wzbogaca treści za pomocą LLM (DeepSeek) oraz embeddingów (qwen3),

## 星数曲线

```mermaid
xychart-beta
    title "miskibin/tygodnik-sejmowy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `eafe3d9dfe0d` · [字段定义](../../DATASET.md)*
