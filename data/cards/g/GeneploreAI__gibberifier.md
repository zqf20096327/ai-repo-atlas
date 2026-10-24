# GeneploreAI/gibberifier

⭐ 118 · HTML · GPL-3.0 · 推送 2026-10-23 · [GitHub](https://github.com/GeneploreAI/gibberifier) · [官网](https://gibberifier.com) · 个人维护

**向文本插入零宽字符、使 LLM 无法正常处理的文本工具**

网页工具，在输入文本的每个字符之间插入数千个不可见的零宽 Unicode 字符：文本外观不变但长度大增，多数 LLM 聊天机器人无法正常加载，表现为崩溃、困惑输出或忽略相关内容。README 建议对约 500 字以内的关键段落使用以降低被检测概率并保持 Google Docs 兼容。另提供 Chrome 与 Firefox 扩展，可在任意网页上对选中文本执行同样操作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在字符间插入零宽 Unicode 字符，视觉不变而长度激增
- 建议对 500 字以内的关键文本使用
- 提供 Chrome 与 Firefox 浏览器扩展

## 适用场景

- 对文本片段做转换，使 LLM 难以处理
- 通过浏览器扩展在网页上直接转换选中文本

## 场景标签

 · 领域:文本工具

## 证据(README 行号)

> L4: **How it works:** This tool inserts thousands of invisible zero-width Unicode characters between each character of y
> L6: **How to use:** This tool works best when gibberifying the most important parts of an essay prompt, up to about 500 

## 星数曲线

```mermaid
xychart-beta
    title "GeneploreAI/gibberifier 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 117 --> 119
    line [118, 118]
```

2026-10-18 118 → 2026-10-24 118（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 low · 依据 README sha `17698c4539c2` · [字段定义](../../DATASET.md)*
