# Gubao-tian/resumepolish

⭐ 6 · JavaScript · MIT · 推送 2026-11-05 · [GitHub](https://github.com/Gubao-tian/resumepolish) · 组织维护 · 中文 README

**面向求职者的单条简历经历按 JD 改写工具**

Web 应用：粘贴一条简历经历与目标岗位 JD，返回改写描述、逐处修改对照、JD 关键词提示与缺失信息反问四项输出。设计上不新增原文没有的事实，服务端做七道输出校验；默认接入 DeepSeek（OpenAI 兼容协议），无 API Key 时进入确定性 Mock 演示模式。前端 React+Vite，后端 Node.js，可部署至 Vercel 或单端口自托管；宣称服务端不落盘、免注册。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单条经历+JD 输入，输出改写文本、修改对照、关键词提示与缺失信息反问
- 服务端七道输出校验，要求每个数字可溯源至原文
- Mock 演示模式：无 API Key 时全链路真实、仅 LLM 调用返回确定性数据
- 166 项 node:test 单测与 GitHub Actions CI 门禁

## 适用场景

- 按目标岗位 JD 改写单条简历经历
- 检查简历关键词与岗位描述的匹配缺口
- 无 API Key 环境下演示或测试改写流程

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: 面向求职者的简历单条经历改写工具：粘贴一条简历经历 + 目标岗位 JD，30 秒内返回四项输出——
> L14: 产品不会新增你原文与补充回答中没有的事实、数字或专有名词；输出中的每个数字都必须可溯源至原文或补充回答（服务端七道校验一票否决）。
> L42: 在 `.env` 中填写 `LLM_API_KEY`（默认 DeepSeek，OpenAI 兼容协议）。`.env` 由 `npm start` 自动加载，


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `a45566a1062c` · [字段定义](../../DATASET.md)*
