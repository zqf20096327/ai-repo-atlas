# maruf009sultan/AIELTS-WRITING

⭐ 23 · TypeScript · MIT · 推送 2026-01-10 · [GitHub](https://github.com/maruf009sultan/AIELTS-WRITING) · [官网](https://ielts-writing-orcin.vercel.app/) · 个人维护

**面向雅思考生与英语学习者的 AI 写作评分与反馈 Web 应用**

基于 React/TypeScript/Vite 的浏览器端 Web 应用：用户粘贴作文、段落或邮件等任意英文文本，调用 OpenAI API 或兼容端点，按雅思四项评分标准（任务完成、连贯衔接、词汇资源、语法多样性）输出单项与总分，逐词逐句标注语法、词汇与句式错误并给出修改，附改进版范文与激励性反馈。API 配置保存在本地浏览器，默认不上传作文数据。需用户提供自己的 API key，通过 git clone 与 npm install 从源码运行。

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

- 按雅思四项标准输出 band scores 与总分
- 词级/句级错误高亮与具体修改建议
- 支持 OpenAI 或任意兼容端点，可在 GPT-4o/3.5-turbo/自定义模型间切换
- API 配置与结果仅存本地浏览器，默认不在服务器存储提交内容

## 适用场景

- 雅思写作练习后即时获得模拟评分与错误分析
- 教师或导师将快速写作分析纳入批改流程
- 对邮件、故事、学术作业等非雅思英文文本获取反馈

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L27: - **Detailed Scoring:** Breaks down your writing with band scores for:
> L51: - Works with your own OpenAI API Key or compatible endpoint.

## 星数曲线

```mermaid
xychart-beta
    title "maruf009sultan/AIELTS-WRITING 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b0468dde4268` · [字段定义](../../DATASET.md)*
