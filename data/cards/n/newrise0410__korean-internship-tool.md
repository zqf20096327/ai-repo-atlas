# newrise0410/korean-internship-tool

⭐ 26 · Python · NOASSERTION · 推送 2026-07-25 · [GitHub](https://github.com/newrise0410/korean-internship-tool) · [官网](https://github.com/newrise0410) · 个人维护

**韩国求职者用的 AI 技能：把招聘 JD 转化为可讲的项目与面试材料**

面向 AI 助手（Claude Code/Codex 等）的技能包加 Python 脚本组合：粘贴韩国招聘公告（Saramin/JobKorea/Wanted/Programmers 均可），先生成能力学习路线图，再从 GitHub 开源候选中按公告匹配度、上手难度、面试话题、运行成本打分排名；脚本扫描仓库生成 audit.json/overview.md 报告，最终产出 STAR 格式简历句、代码讲解稿、面试问答与检查清单。评分脚本不自行判断文本，需 AI 助手填写各分项分数。覆盖后端/前端/移动/AI 等开发岗位。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- JD 输入后按匹配度/上手难度/面试话题等维度对开源候选打分排名
- chwieop-scan 等三个命令扫描仓库生成结构与依赖报告
- 产出 STAR 简历句、代码讲解稿与面试问答等材料
- 支持 taste.json 偏好文件与四种执行深度（interview-only 到 remote-full-run）

## 适用场景

- 看到招聘公告但不知道做什么项目的求职者生成可讲的项目方案
- 为所选开源项目准备简历句子和面试问答
- 在 AI 助手里按公告逐步完成项目选定、代码分析与面试准备

## 场景标签

 · 领域:职业发展/开发者工具

## 证据(README 行号)

> L18: 채용공고 하나를 던지면, **지원서에 쓸 수 있고 면접에서 설명할 수 있는 프로젝트**까지 데려다주는 AI 어시스턴트용 스킬입니다.
> L20: 프로젝트를 처음부터 만들지는 않습니다. 공고에 맞는 GitHub 오픈소스를 골라주고, 그 코드를 파악하는 법을 알려주고, 면접에서 이야기할 만한 부분을 직접 손보게 안내합니다. 마지막엔 이력서 문장과 예상 
> L83: > Codex를 쓰면서 Plan 모드를 켜는 걸 권합니다. 그래야 선택지가 팝업으로 제대로 뜹니다. 다른 도구도 Plan이나 Ask 모드가 있으면 켜두세요. 없으면 그냥 텍스트로 묻고 답하는 형태가 됩니다.

## 星数曲线

```mermaid
xychart-beta
    title "newrise0410/korean-internship-tool 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `57ed9555e4eb` · [字段定义](../../DATASET.md)*
