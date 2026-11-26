# lunw/shopify-to-shopline-theme-migration

⭐ 3 · JavaScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/lunw/shopify-to-shopline-theme-migration) · 个人维护 · 中文 README

**供 AI 智能体使用的 Shopify 主题迁移到 SHOPLINE 的技能包**

以 agent skill 形式发布的迁移指南包，智能体加载 SKILL.md 后按流程将 Shopify（Liquid/JSON）主题的模板层转换为 SHOPLINE OS 3.0（SLine）格式。内容覆盖语法转换、文件结构、CSS 变量对齐、数据访问逻辑与 i18n 键校验，并收录约二十种静默失败模式（字段缺失不报错、页面渲染空白）。仅处理模板层，不含内容填充、页面映射与商店配置；迁移后需重建主题。要求安装 SHOPLINE AI Suite 四个技能与 SHOPLINE CLI，Shopify 侧 toolkit 为可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SKILL.md 入口 + 按需加载的 references 结构，共 10 条静默失败规则
- 对象字段映射与静默失败目录：语法相同但字段不同导致页面空白
- 经真实迁移验证：253 文件、19 模板、30 sections、34 locales
- 附 scripts/sl.sh 处理代理环境下 CLI 返回 HTTP 400 的问题

## 适用场景

- 让智能体把现有 Shopify 主题模板层迁移到 SHOPLINE OS 3.0
- 迁移后排查页面渲染空白等静默失败问题
- 以官方 Fashion1 主题为参照核对不确定的对象字段

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L6: agent skill
> L10: An agent skill for porting a **Shopify theme template layer** to **SHOPLINE OS 3.0** (SLine),
> L89: The agent loads `SKILL.md` when a request matches its description; references are loaded on


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `cc72f241342c` · [字段定义](../../DATASET.md)*
