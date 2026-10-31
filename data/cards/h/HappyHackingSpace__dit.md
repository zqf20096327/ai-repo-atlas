# HappyHackingSpace/dit

⭐ 18 · Go · MIT · 推送 2026-10-23 · [GitHub](https://github.com/HappyHackingSpace/dit) · 组织维护

**ML 分类 HTML 页面/表单/字段类型的 Go 库与 CLI**

基于逻辑回归与 CRF 的 Go 库及命令行工具：对 HTML 页面分类（login、error、soft_404 等 21 类）、识别表单类型（登录/搜索/注册/密码找回等）、并分类各字段（用户名、密码、邮箱等 79 种字段类型代码）。零外部 ML 依赖，模型加载自 model.json，数据通过 dit data download 获取。10 折交叉验证：表单准确率 82.9%，字段 86.6%，页面 53.4%；训练集为 1000+ 标注表单与 754 标注页面。为 katana、httpx 等爬虫工具所用，系 Formasaurus 的 Go 移植。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 页面/表单/字段三层分类，覆盖 79 种字段类型代码
- 零外部 ML 依赖（LogReg + CRF 自实现）
- 提供 Go 库与 CLI 两种使用方式
- 报告 10 折分组交叉验证准确率

## 适用场景

- 爬虫/安全扫描中自动识别登录、验证码、WAF 拦截等页面类型
- 批量自动填写或分析网页表单时判断字段含义
- Web 数据抽取流程中区分表单用途

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L4: **dît** (means *found* in Kurdish) tells you the type of an HTML page, form, and fields using machine learning.
> L6: It classifies pages (login, error, landing, blog, etc.), detects whether a form is a login, search, registration, pa

## 星数曲线

```mermaid
xychart-beta
    title "HappyHackingSpace/dit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-31 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4019e9008d6f` · [字段定义](../../DATASET.md)*
