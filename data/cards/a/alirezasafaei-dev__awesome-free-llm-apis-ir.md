# alirezasafaei-dev/awesome-free-llm-apis-ir

⭐ 14 · JavaScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/alirezasafaei-dev/awesome-free-llm-apis-ir) · [官网](https://llm.persiantoolbox.ir/) · 个人维护

**面向伊朗用户的免费 LLM API 目录：配额与可达性机器可读编目**

波斯语优先、机器可读的免费 LLM API 聚合目录：收录 26 个 Provider/Gateway 服务，逐项记录免费类型（永久配额/月度额度/试用）、RPM/RPD/TPM 限制、是否需要国际银行卡、OpenAI 兼容性与 Base URL、以及从伊朗直接访问或需 VPN 的状态（须有日期化的测试证据）。数据以 data/providers 独立文件加 JSON Schema 维护，生成 catalog.json 与 README 表格，CI 校验、每周上游监视并标记过期记录；另含伊朗实测工具、波斯语基准（15 测例 5 类）与代理/桥接工具的独立风险目录。面向波斯语开发者社区，通过 git clone 与 npm 脚本运行。

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

- 26 个免费 LLM API 的配额、注册前置与 OpenAI 兼容性编目
- 伊朗访问状态 8 级证据体系（直接测试/VPN/官方封锁等，须日期化记录）
- 机器可读：data/providers + JSON Schema 生成 catalog.json，CI 与每周上游监视防过期
- 内置伊朗 IP 实测工具与本地评分的波斯语基准（15 测例）

## 适用场景

- 伊朗境内开发者查找无需国际银行卡且可直接访问的免费 LLM API
- 网站或工具直接消费 catalog.json 获取机器可读的 Provider 数据
- 查询各服务免费层与 Trial/Credit 的区别及速率限制

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L10: فهرست آزاد، فارسی و ماشین‌خوان از APIهای رایگان مدل‌های زبانی؛ با تمرکز ویژه بر **محدودیت مصرف، توکن، نیاز به پرداخ
> L122: هر سرویس یک فایل مستقل در `data/providers` دارد و ساختار آن با `schema/provider.schema.json` تعریف شده است. وب‌سای

## 星数曲线

```mermaid
xychart-beta
    title "alirezasafaei-dev/awesome-free-llm-apis-ir 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `6af87e34a418` · [字段定义](../../DATASET.md)*
