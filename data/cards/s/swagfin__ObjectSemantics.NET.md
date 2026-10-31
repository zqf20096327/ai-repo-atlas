# swagfin/ObjectSemantics.NET

⭐ 14 · C# · MIT · 推送 2026-09-16 · [GitHub](https://github.com/swagfin/ObjectSemantics.NET) · 个人维护

**.NET 模板引擎：把对象数据渲染成个性化邮件/收据/报告**

面向 .NET 开发者的轻量模板库：用小型模板语言（占位符、嵌套属性、循环、条件、算术、聚合、格式化）将 POCO 对象渲染为邮件、通知、收据和报告文本。模板可编译后跨并发渲染复用，支持 TextWriter 流式输出。提供模板校验诊断、StrictMode、嵌套/长度/迭代/输出限制、XML 转义、可配置缓存等生产控制项。README 附 BenchmarkDotNet 测量数据，并说明部分新能力在 NuGet 发布前需从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模板语言支持嵌套属性、循环、条件、算术与 sum/avg/min/max/count 聚合
- Compile() 编译一次可跨并发渲染复用，支持 TextWriter 流式输出
- 模板校验诊断 + StrictMode + 嵌套/模板/迭代/输出四类限额
- 进程级模板缓存可配置容量与源字符预算

## 适用场景

- 用一份模板生成催款提醒、订单确认、收据等个性化消息
- 通知服务中预编译模板后按不同模型批量渲染
- 对用户提交的模板先校验语法、限额后再渲染

## 场景标签

 · 领域:软件开发/模板与格式化

## 证据(README 行号)

> L14: ObjectSemantics.NET is a lightweight .NET templating library that turns objects into personalized emails, notificat
> L29: dotnet add package ObjectSemantics.NET

## 星数曲线

```mermaid
xychart-beta
    title "swagfin/ObjectSemantics.NET 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 low · 依据 README sha `d57c2d8026d3` · [字段定义](../../DATASET.md)*
