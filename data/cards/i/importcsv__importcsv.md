# importcsv/importcsv

⭐ 111 · TypeScript · NOASSERTION · 推送 2026-03-15 · [GitHub](https://github.com/importcsv/importcsv) · [官网](https://docs.importcsv.com) · 组织维护

**带 AI 列映射的 React CSV 导入组件**

面向 React 应用的 CSV/Excel 导入组件，提供虚拟滚动处理大文件、内置校验器（邮箱/电话/日期/正则）与数据清洗变换。分两种模式：Local Mode 全部在浏览器运行、无需后端，列映射用模糊字符串匹配；Backend Mode 增加基于 OpenAI 的自动列映射、自然语言数据修正（BAML 模板 + LiteLLM）、Redis Queue 后台处理 1GB+ 文件与 Webhook 通知。AI 功能仅限 Backend Mode 且需 OpenAI API key，自然语言命令仅支持英文，无 Vue/Angular 版本。前端 MIT、后端 AGPL-3.0 双许可并另提商业许可选项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 虚拟滚动在浏览器内处理至 10 万行数据
- OpenAI 自动列映射（含置信度分数与 Redis 缓存）
- 自然语言数据修正（如“修正所有邮箱”），逐项变更供用户确认
- Backend Mode 支持 Redis Queue 后台处理 1GB+ 文件与 Webhook 通知

## 适用场景

- 在我的 React 应用里快速加上带校验的 CSV 导入功能
- 把用户上传的 CSV 列自动映射到我的数据库 schema
- 用自然语言批量修正导入数据中的格式问题
- 生产环境后台处理大体积 CSV 文件并回调通知

## 场景标签

 · 领域:Web 前端组件/数据导入工具

## 证据(README 行号)

> L13: A React component that handles CSV imports with automatic column mapping and data validation.
> L17: - **Backend Mode**: Adds AI column mapping and natural language transformations with OpenAI.
> L219: **Note:** AI features are only available in Backend Mode. In Local Mode, column mapping uses fuzzy string matching

## 星数曲线

```mermaid
xychart-beta
    title "importcsv/importcsv 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 110 --> 112
    line [111, 111]
```

2026-10-18 111 → 2026-10-27 111（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `69c70fe63a24` · [字段定义](../../DATASET.md)*
