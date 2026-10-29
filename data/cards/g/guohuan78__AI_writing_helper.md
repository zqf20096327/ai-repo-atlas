# guohuan78/AI_writing_helper

⭐ 32 · Python · 推送 2026-08-29 · [GitHub](https://github.com/guohuan78/AI_writing_helper) · 个人维护 · 中文 README

**公众号作者的 AI 推文创作台：选题到成稿一条生产线**

在网页中完成公众号推文全流程的工具：选题（一次 6 个角度）、标题（8 个候选）、大纲、逐段流式成稿、5 档强度润色（3 版并排对比）、120 字摘要与封面创意，导出带 YAML front matter 的 Markdown，可对接 wechat-publisher 完成排版预览、存草稿送审与发表状态回显。模型调用走 OpenAI 兼容协议，支持 OrcaRouter、StepFun、智谱 GLM、Kimi 等供应商切换。本地 SQLite 语料库按 bigram 相关度注入文风参考并记录选题避重历史。交互与一键自动两种模式，Python 3.10+ 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 选题→标题→大纲→逐段成稿→摘要→导出的 8 步流水线，支持一键无人干预自动模式
- 多供应商切换：OrcaRouter/StepFun/智谱 GLM/Kimi/自定义 OpenAI 兼容地址，Key 独立保存
- SQLite 语料库按字符 bigram 检索注入文风参考，同主题已用角度自动避开
- 对接 wechat-publisher 实现排版预览、草稿送审与审批状态回显

## 适用场景

- 我要从零写一篇公众号推文，让 AI 帮我出角度、标题和初稿
- 我想让成稿保持自己过往文章的语气与节奏
- 写完直接排版存草稿送审，不用在多个工具间来回切换

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5: 面向公众号作者的推文创作工具：从选题到成稿的一条生产线，在网页里完成选题、标题、大纲、逐段成稿和摘要，导出带 YAML front matter 的 Markdown，可直接交给 wechat-publisher 自动排版、存草稿、
> L19: 4. **成稿**：按大纲逐段流式生成，边写边出字；语料库有存货时自动注入文风参考。
> L31: 模型调用统一走 OpenAI 兼容协议（官方 OpenAI SDK），「设置」里切换供应商即可，每个供应商的 Key 独立保存（`config.json` 的 `api_keys`），切换时自动载入对应 Key、官方地址与默认模型

## 星数曲线

```mermaid
xychart-beta
    title "guohuan78/AI_writing_helper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-29 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4d68c0bcd841` · [字段定义](../../DATASET.md)*
