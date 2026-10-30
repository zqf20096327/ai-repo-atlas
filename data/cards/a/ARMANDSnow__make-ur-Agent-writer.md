# ARMANDSnow/make-ur-Agent-writer

⭐ 20 · Python · NOASSERTION · 推送 2026-09-16 · [GitHub](https://github.com/ARMANDSnow/make-ur-Agent-writer) · 个人维护 · 中文 README

**本地多 agent 长篇小说续写流水线，研究性质个人创作工具**

将知识抽取、情节规划、正文生成、审稿与关系推进拆为可恢复步骤的多 agent 小说续写工具：导入原作 txt 或 EPUB，自动切章、抽取人物/事件/关系知识，经情节辩论与章节规划后逐章生成正文，配 5+1 reviewer、确定性 lint、文风漂移检测与伏笔管理；支持长跑断点恢复、预算守门与本地 Web 工作台。开发与标准验收默认 mock 不产生计费请求，真实模型经 LiteLLM 以 OpenAI 兼容接口接入。声明为研究性质个人创作工具，非公网多租户产品；10–20 章长跑稳定性待验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 九阶段流水线：导入/切章→知识抽取→规划→写作→审核→关系推进→滚动续写
- 5+1 reviewer、确定性 lint、文风指纹与漂移检测
- supervisor/heartbeat/watchdog 支持长跑断点恢复
- 本地 Web 四阶段工作台，验收默认 mock 模式零计费

## 适用场景

- 导入已有小说语料进行人机协同续写
- 原创长篇小说的规划、写作与审稿管理
- 在本地以受控预算长跑生成并审校多章内容

## 场景标签

`AI 写作` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7: 本地运行的多 agent 小说续写流水线。它将知识抽取、情节规划、正文生成、审稿和关系推进拆成可恢复步骤；开发与标准验收默认使用 mock，不产生计费模型请求。
> L17: - 小说原创与导入续写：权威 `creation_mode`、起点安全视图、知识提案、情节辩论、章节规划、写作与评审。
> L130: 这是研究性质的个人创作工具，不是公网多租户产品。原作小说不重新分发，生成内容和本地运行数据不提交。技术栈为 Python 3.9+、LiteLLM、Pydantic、tiktoken、python-dotenv；Web 使用标准

## 星数曲线

```mermaid
xychart-beta
    title "ARMANDSnow/make-ur-Agent-writer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `ea94e0564bca` · [字段定义](../../DATASET.md)*
