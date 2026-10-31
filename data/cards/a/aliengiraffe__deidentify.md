# aliengiraffe/deidentify

⭐ 41 · Go · MIT · 推送 2026-08-20 · [GitHub](https://github.com/aliengiraffe/deidentify) · 组织维护

**Go 库：检测文本与结构化数据中的个人身份信息并做确定性匿名化替换**

由 AlienGiraffe, Inc. 维护的开源 Go 包，检测文本、表格与 CSV 类切片数据中的 PII（姓名、邮箱、电话、SSN、信用卡、地址），并以保持原格式的替身值替换；替换是确定性的——相同输入与密钥产生相同输出，从而保留跨记录/跨运行的引用一致性。使用列名作为上下文防止关联，线程安全。替换表含 110+ 中性名、130+ 姓氏、105+ 虚构邮箱域名、120+ 街道名，支持多地区地址格式。README 声明不保证 100% 检测率，默认保留电话区号。通过 go get 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性替换：相同输入与密钥产生相同输出，保留引用一致性
- 格式保持替换，支持 6 类 PII（姓名/邮箱/电话/SSN/信用卡/地址）
- 表格与 CSV 切片结构化数据处理，列名作为上下文防关联
- 国际地址格式支持（北美/欧洲/亚洲/中东等）

## 适用场景

- 数据对外交付或共享前匿名化含 PII 的数据集
- LLM 输入预处理时去除文本中的个人敏感信息
- 跨记录保持同一人指向同一替身值，维护数据可用性

## 场景标签

 · 领域:数据安全/隐私工程

## 证据(README 行号)

> L10: A Go library for detecting and removing personally identifiable information (PII) from text and structured data.
> L14: `deidentify` is an open source Go package, created by AlienGiraffe, Inc., that detects personally identifiable info
> L18: - **Multiple PII types support**: Emails, phone numbers, SSNs, credit cards, names, and addresses

## 星数曲线

```mermaid
xychart-beta
    title "aliengiraffe/deidentify 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-31 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `1ed16f91e79a` · [字段定义](../../DATASET.md)*
